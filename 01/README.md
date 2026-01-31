<style>
    .result-table {
        border-collapse: collapse;
        width: 100%;
        max-width: 600px;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }

    .result-table th {
        background-color: #D6E4F2;
        color: #000;
        font-weight: bold;
        padding: 10px;
        border: 1px solid #A0A0A0;
        text-align: center;
    }

    .result-table td {
        background-color: white;
        color: #000;
        padding: 12px 15px;
        border: 1px solid #A0A0A0;
        color: #333;
        font-size: 1.3em;
        font-weight: bold;
    }

    /* 첫 번째 열(입력)과 두 번째 열(출력)의 너비를 동일하게 설정 */
    .result-table th,
    .result-table td {
        width: 50%;
    }
</style>

<div class="page-content tex2jax_process">
    <h1>문제 01 배열 정렬하기★</h1>
    <p>저자 권장 시간 _ 10분 | 권장 시간 복잡도 _ O(NlogN) | 출제 _ 저자 출제</p>
    <p><a href="https://github.com/dremdeveloper/codingtest_python/blob/main/solution/01.py" data-google-vignette="false">깃허브 URL</a></p>
    <hr>
    <p>정수 배열을 정렬해서 반환하는 solution( ) 함수를 완성하세요.</p>
    <h3 id="_1">제약조건</h3>
    <ul>
        <li>정수 배열의 길이는 2 이상 105 이하입니다.</li>
        <li>정수 배열의 각 데이터 값은 -100,000 이상 100,000 이하입니다.</li>
    </ul>
    <h3 id="_2">입출력의 예</h3>
    <table class="result-table">
        <thead>
            <tr>
                <th>입력</th>
                <th>출력</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>[1, -5, 2, 4, 3]</td>
                <td>[-5, 1, 2, 4, 3]</td>
            </tr>
            <tr>
                <td>[2, 1, 1, 3, 2, 5, 4]</td>
                <td>[1, 1, 2, 2, 3, 4, 5]</td>
            </tr>
            <tr>
                <td>[6, 1, 7]</td>
                <td>[1, 6, 7]</td>
            </tr>
        </tbody>
    </table>
    <h3 id="_3">문제 분석하고 풀기</h3>
    <p><strong>문제만 놓고 보면 간단해 보이지만 제약 조건은 주의 깊게 봐야 합니다.</strong> 제약 조건을 보면 데이터 개수는 최대 105입니다. 즉, 제한 시간이 3초라면 O(N2) 알고리즘은 사용할 수 없습니다. 만약 정수 배열의 최대 길이가 10이라면 O(N2) 알고리즘을 사용해도 되죠. 제가 이 문제를 제시한 이유는 제약 조건에 따른 알고리즘의 선택을 보여주기 위함입니다. 이렇게 제약 조건에 따라 같은 문제도 난이도가 달라질 수 있습니다. 그리고 이런 때에 초보자가 하기 쉬운 실수는 너무 문제가 쉽다고 생각해서 제약 조건을 고려하지 않는다는 겁니다. 단순히 내림차순 또는 오름차순으로 정렬하면 이 문제는 통과할 수 없습니다. <strong>정답 코드는 다음과 같이 아주 짧습니다.</strong></p>
    <pre><code>
def solution(arr):
    arr.sort()
    return arr
</code></pre>
    <p>sort( ) 메서드는 리스트를 역순으로 반환합니다. <strong>주목할 점은 sort( ) 메서드가 리스트 원본 자체의 값을 바꾼다는 겁니다.</strong> 만약 원본 리스트를 그대로 두고 싶다면 다음과 같이 구현하면 됩니다.</p>
    <pre><code>
def solution(arr):
    sorted_list = list(sort(arr))
    return sorted_list 
</code></pre>
    <hr>
    <h3 id="sort-on2">[합격조언] sort( ) 메서드를 사용하지 않고 O(N<sup>2</sup>) 정렬 알고리즘을 사용하면?</h3>
    <p>sort( ) 메서드를 사용하지 않고 O(N<sup>2</sup>) 정렬 알고리즘으로 배열 원소를 정렬하는 연산을 구현하면 시간 차이는 얼마나 벌어질까요? 다음 코드를 봅시다.</p>
    <pre><code>
import time
<br>
def bubble_sort(arr):  # 버블 정렬로 정렬하기
    n = len(arr)
        for i in range(n):
            for j in range(n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr
<br>
def do_sort(arr):  # sort( ) 함수로 배열 정렬하기
    arr.sort( ) 
    return arr
<br>
def measure_time(func, arr):  # 시간을 측정하고 뒤집힌 배열 반환
    start_time = time.time( ) 
    result = func(arr)
    end_time = time.time( ) 
    return end_time - start_time, result
<br>
arr = list(range(10000))
<br>
#첫 번째 코드 시간 측정
#첫 번째 코드 실행 시간 : 3.9616279602
bubble_time, bubble_result = measure_time(bubble_sort, arr)
print("첫 번째 코드 실행 시간:", format(bubble_time, ".10f"))
<br>
#두 번째 코드 시간 측정
#두 번째 코드 실행 시간 : 0.0000560284
arr = list(range(10000))
reverse_time, reverse_result = measure_time(do_sort, arr)
print("두 번째 코드 실행 시간:", format(sort_time, ".10f"))
<br>
#두 개의 코드의 결과가 동일한지 확인
print("두 개의 코드의 결과가 동일한지 확인:", bubble_result == sort_result)  # True 
</code></pre>
    <p>sort( ) 메서드는 리스트를 역순으로 반환합니다. <strong>주목할 점은 sort( ) 메서드가 리스트 원본 자체의 값을 바꾼다는 겁니다.</strong> 만약 원본 리스트를 그대로 두고 싶다면 다음과 같이 구현하면 됩니다.</p>
    <p>첫 번째 방법은 O(N<sup>2</sup>) 정렬 알고리즘인 버블 정렬을 활용한 방법이고, 두 번째 방법은 O(NlogN) 시간 복잡도의 sort( ) 함수를 활용한 방법입니다. 결과를 보면 시간 차가 상당합니다. 데이터 10,000개를 역순으로 정렬하는 데 버블 정렬은 4초가 걸렸지만 sort( ) 함수를 활용한 두 번째 방법은 1초도 걸리지 않았습니다. 실행 환경마다 시간의 차이는 조금 생길 수 있겠지만 압도적으로 sort( ) 함수가 성능이 좋다는 것을 알 수 있습니다. 이것으로 알고리즘의 시간 복잡도가 얼마나 중요한지 알아두기 바랍니다.</p>
    <hr>
    <h3 id="_4">시간 복잡도 분석하기</h3>
    <p>N은 arr의 길이이므로 시간 복잡도는 O(NlogN)입니다.</p>

</div>