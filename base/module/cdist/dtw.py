def dtw(x, y, dist, warp=1):
    """
            Computes Dynamic Time Warping (DTW) of two sequences.
                :param array x: N1*M array
                    :param array y: N2*M array
                        :param func dist: distance used as cost measure
                            :param int warp: how many shifts are computed.
                                Returns the minimum distance, the cost matrix, the accumulated cost matrix, and the wrap path.
                                    """
                                        assert len(x)
                                            assert len(y)
                                                r, c = len(x), len(y)
                                                    D0 = zeros((r + 1, c + 1))
                                                        D0[0, 1:] = inf
                                                            D0[1:, 0] = inf
                                                                D1 = D0[1:, 1:]  # view
                                                                    for i in range(r):
                                                                        for j in range(c):
                                                                            D1[i, j] = dist(x[i], y[j])
                                                                                                    C = D1.copy()
                                                                                                        for i in range(r):
                                                                                                            for j in range(c):
                                                                                                                min_list = [D0[i, j]]
                                                                                                                                                for k in range(1, warp + 1):
                                                                                                                                                    i_k = min(i + k, r - 1)
                                                                                                                                                                                    j_k = min(j + k, c - 1)
                                                                                                                                                                                                    min_list += [D0[i_k, j], D0[i, j_k]]
                                                                                                                                                                                                                D1[i, j] += min(min_list)
                                                                                                                                                                                                                    if len(x)==1:
                                                                                                                                                                                                                        path = zeros(len(y)), range(len(y))
                                                                                                                                                                                                                    elif len(y) == 1:
                                                                                                                                                                                                                        path = range(len(x)), zeros(len(x))
                                                                                                                                                                                                                    else:
                                                                                                                                                                                                                        path = _traceback(D0)
                                                                                                                                                                                                                                                                    return D1[-1, -1] / sum(D1.shape), C, D1, path

