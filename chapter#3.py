# 팬더스를 활용한 데이터 분석
# 넘파이와 팬더스는 데이터 분석에 필요한 필수 라이브러리이다.
# 상관계수 계산 및 상관계수에 따른 리스크의 완화효과를 알아본다
# 넘파이 배열 
# 넘파이  = Numerical Python의 줄임말
# 파이션으로 수치해석이나 통계 관련 작업을 구현할때 가장 기본이 되는 모듈이다.
# 넘파이는 ndarray라는 고성능 다차원 배열 객체와 이를 다루는 여러 함수를 제공한다.
# 차원을 나타내는 ndim 속성과 각 차원의 크기를 튜플로 나타내는 shape 속성을 지닌다.
# dtype 원소 자료형 속성
# 원소별 최대값,최소값,평균값,합계를 구하는 함수도 있다.
#        max    min    mean  sum
# 리스트를 인수로 받아서 배열을 생성하는 array()함수를 제공한다.
import numpy as np
A = np.array([[1,2],[3,4]])
print(A)
print(A.ndim)
print(A.shape)
print(A.dtype)

print(A.max(),A.min(),A.mean(),A.sum())
print(A[0],A[1],A[0][0])
print(A[A>1])           # 조건에 맞는 인덱싱할 수도 있다

# 전치 : 배열의 요소 위치를 주대각선을 기준으로 뒤바꾸는 것
# trnspose() 함수 사용

print(A.T , A.transpose())

# flatten()  다차원 배열을 1차원 배열 형태로 

print(A.flatten())
