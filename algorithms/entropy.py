import numpy as np
import numpy

def matrix_standardization(M):
    # if M != numpy.ndarray:
    #     msg = "input is not a numpy ndarray!"
    #     raise Exception(msg)
    # standardize the input matrix (最大最小标准化)
    M = M.copy()
    M = (M - M.min()) / (M.max() - M.min())
    return M

def get_entropy(M):
    # get the column number and row number (m,n为矩阵行和列数)
    m, n = M.shape
    k = 1 / np.log(m)
    # Add by column (axis=0列相加 axis=1行相加)
    yij = M.sum(axis=0) 
    # pij为yij的先验概率
    pij = M / yij
    # 
    test = pij * np.log(pij)
    # Replace nan with 0 (将nan空值转换为0）
    test = np.nan_to_num(test)
    # Calculate the entropy of each column (计算每列信息熵)
    ej = -k * (test.sum(axis=0))
    # Calculate the weights (计算每种指标的权重)
    wi = (1 - ej) / (n - np.sum(ej))
    
    return ej, wi, 


def get_score(M, W):
    W = W.copy()
    M = M.copy()
    # Calculate the scores （计算得出最终得分）
    S = W * M
    return S.sum(axis=0)