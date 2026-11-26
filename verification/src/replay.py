#!/usr/bin/env python3
"""Replay the 3-PARTITION instances using exact rational block costs."""
from fractions import Fraction as F
from itertools import product


def target(m, j):
    return F(1, 4) + F(j, 12*m)


def pair(m, b, j):
    mass = 120*m*m*b
    q = target(m, j)
    mean = q - (1-q)*F(b, mass)
    return mass, q, mean


def atoms(weights, b):
    m = len(weights)//3
    data = [(F(a), 1, F(0)) for a in weights]
    for j in range(1, m+1):
        mass, q, mean = pair(m, b, j)
        label_one = mass*mean
        label_zero = mass*(1-mean)
        assert min(label_one, label_zero) >= F(mass, 5)
        data += [(label_one, 1, q), (label_zero, 0, q)]
    assert sum(w for w, _, _ in data) == m*(120*m*m*b+b)
    return data


def partitions(n):
    """Generate each set partition once as a tuple of nonempty bitmasks."""
    if n == 0:
        yield ()
        return
    new = 1 << (n-1)
    for prior in partitions(n-1):
        yield prior + (new,)
        for i, block in enumerate(prior):
            yield prior[:i] + (block | new,) + prior[i+1:]


def block_cost(block):
    p = sum(w*y for w, y, _ in block) / sum(w for w, _, _ in block)
    return sum(w*abs(f-p) for w, _, f in block)


def exact_minimum(weights, b):
    assert len(weights) == 6 and sum(weights) == 2*b
    assert all(F(b, 4) < a < F(b, 2) for a in weights)
    data = atoms(weights, b)
    n = len(data)
    costs = [F(0)] + [
        block_cost([atom for i, atom in enumerate(data) if mask & (1 << i)])
        for mask in range(1, 1 << n)
    ]
    optimum, count = F(sum(w for w, _, _ in data)), 0
    for partition in partitions(n):
        optimum = min(optimum, sum(costs[mask] for mask in partition))
        count += 1
    assert count == 115975
    return optimum, count


def anchor_cost(m, b, j, load):
    anchor_mass, q, mean = pair(m, b, j)
    p = (anchor_mass*mean+load)/(anchor_mass+load)
    return load*p + anchor_mass*abs(p-q)


def test_loss_identities():
    checks = 0
    for m, b in product(range(1, 7), range(1, 22)):
        for j in range(1, m+1):
            mass, q, mean = pair(m, b, j)
            assert min(mean, 1-mean) >= F(1, 5)
            for load in range(m*b+1):
                cost = anchor_cost(m, b, j, load)
                if load <= b:
                    exact = load*q + (1-q)*F((b-load)*(mass-load), mass+load)
                    assert cost == exact >= b*q - F(b-load, 3)
                else:
                    assert cost == b*q + load-b
                checks += 1
    return checks


def check_all_assignments(weights, b):
    """The ordinary-only bucket is index 0; the two anchors are indices 1 and 2."""
    K = b*(target(2, 1)+target(2, 2))
    balanced = False
    minimum = None
    for where in product(range(3), repeat=len(weights)):
        load = [sum(a for a, index in zip(weights, where) if index == j) for j in range(3)]
        deficiency = sum(max(b-s, 0) for s in load[1:])
        excess = sum(max(s-b, 0) for s in load[1:])
        assert deficiency == excess+load[0]
        cost = load[0] + sum(anchor_cost(2, b, j, load[j]) for j in (1, 2))
        assert cost >= K+F(2, 3)*deficiency
        if deficiency == 0:
            assert load == [0, b, b]
            balanced = True
        minimum = cost if minimum is None else min(minimum, cost)
    return balanced, minimum


def main():
    variants = (
        (15, (4, 4, 5, 5, 6, 6), True),
        (15, (4, 4, 4, 6, 6, 6), False),
        (12, (4, 4, 4, 4, 4, 4), True),
    )
    for b, weights, feasible in variants:
        optimum, partitions_checked = exact_minimum(weights, b)
        balanced, best_anchored = check_all_assignments(weights, b)
        K = b*(target(2, 1)+target(2, 2))
        assert optimum == best_anchored
        assert balanced == feasible == (optimum == K)
        assert feasible or optimum >= K+F(2, 3)
        total = 2*(120*4*b+b)
        print(f"B={b}, weights={weights}: {partitions_checked:,} partitions; "
              f"loss={optimum}, excess={optimum-K}, normalized distance={optimum/total}.")
    witnessed_no = anchor_cost(2, 15, 1, 16) + anchor_cost(2, 15, 2, 14)
    assert witnessed_no == F(308925, 28856)
    print(f"Checked {test_loss_identities():,} exact single-block load identities.")
    print("PASS: intact-pair witnesses, full partitions, and the 2/3 deficit bound.")


if __name__ == "__main__":
    main()
