#백준 9024

#주어지는 수의 범위가 K,N에 비해 작아 무시가능하다는 가정,
#최악의 시간복잡도 O(N)

def prob1() :
    N, K = map(int,input().split())
    nums = list(map(int, input().split()))
    nums = sorted(nums)
    nums_set = set(nums)
    
    count = 0

    #예외처리
    if(len(nums) <= 1 ) :
        print("두 개 이상의 값을 입력해주세요")
        return


    #K가 최대합과 최소합에서 멀리 떨어져 있을 경우 diff가 커져 시간복잡도적 측면에서 무시 불가 -> 분리
    
    #이 조건문을 통과하면, K가 합의 쌍 범위 내에 존재,
    if ( nums[-1] + nums[-2] < K or nums[0] + nums[1] > K ) :
        print(1)
        return


    #diff = abs(K - (n + k)), 합의 범위 이내의 값
    #min(K- 합의 최소값 또는 K - 합의 최대값)으로 시작,  작아지면 갱신
    #값을 find하는 데 list 대신 set을 사용하여 O(1)로 검사가능

    #O(N)*O(diff)*O(1) -> diff 무시가능    
    diff = min(abs(K - (nums[-1] + nums[-2])), abs(K - (nums[0] + nums[1])))
    diff_tmp = diff
    for n in nums :
        diff = diff_tmp
        for k in range(K - diff - n, K + diff + 1 - n) :
            if k in nums_set :
                if (n == k) :
                    continue
                elif (k == K - diff_tmp - n) or (k == K + diff_tmp - n) :
                    count += 1
                else :
                    if (abs(K - n - k) < diff) :
                        diff_tmp = abs(K - n - k)
                        count = 1



                    
    #중복된 값에 대한 제거 (a,b) (b,a)
    print(count//2)

t = int(input())
for i in range(t):
    prob1()