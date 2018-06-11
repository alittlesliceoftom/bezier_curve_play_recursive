import numpy as np

def linterp(a,b,t):
    '''
    :param a: pnt 1
    :param b: pnt 2
    :param t: time
    :return:
    '''
    return a


def bezier(pnts,t):
    if len(pnts) == 1:
        return pnts
    else:
        subset
        return bezier(pnts)


def random_control_pnts(n = 3, pnts = []):
    print (pnts)
    try:
        print(len(pnts))
        if len(pnts)/2 == n:
            return pnts
    except:
        pass
    else:
        return random_control_pnts(n, np.append(pnts,[np.random.rand(1,2) ] ) )