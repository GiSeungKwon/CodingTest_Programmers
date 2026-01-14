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
    <h1>문제 03 두 개 뽑아서 더하기★</h1>
    <p>정답률 _ 68% | 저자 권장 시간 _ 30분 | 권장 시간 복잡도 _ O(N2log(N2)) | 출제 _ 월간 코드 챌린지</p>
    <hr>
    <p>정수 배열 numbers가 주어집니다. numbers에서 서로 다른 인덱스에 있는 2개의 수를 뽑아 더해 만들 수 있는 모든 수를 배열에 오름차순으로 담아 반환하는 solution( ) 함수를 완성하세요.</p>
    <h3 id="_1">제약조건</h3>
    <ul>
        <li>numbers의 길이는 2 이상 100 이하입니다.</li>
        <li>numbers의 모든 수는 0 이상 100 이하입니다.</li>
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
                <td>[2,1,3,4,1]</td>
                <td>[2,3,4,5,6,7]</td>
            </tr>
            <tr>
                <td>[5,0,2,7]</td>
                <td>[2,5,7,9,12]</td>
            </tr>
        </tbody>
    </table>
    <h3 id="_3">문제 분석하고 풀기</h3>
    <p>문제 자체에 요구사항이 그대로 드러나 있는 난이도가 낮은 문제입니다. 숫자 배열에서 서로 다른 두 수를 선택해서 더한 결과를 모두 구하고 오름차순으로 정렬해서 반환하면 됩니다. 하나 놓치기 쉬운 점은 중복값은 허용하지 않는다는 겁니다. 테스트 케이스를 보면 입력값 [5, 0, 2, 7]에 대해 반환값이 2 + 5, 0 + 7으로 7이 둘이 아니라 하나입니다. 이런 간단한 함정은 여러분이라면 쉽게 피할 수 있을 것이라 생각합니다만 이렇게 입출력값에 대해서는 일부러라도 분석하는 시간을 반드시 가져보기 바랍니다. numbers의 최대 데이터 개수는 100이므로 시간 복잡도는 고려하지 않아도 되겠네요. 그렇다면 이 문제는 다음과 같은 과정으로 풀 수 있습니다.</p>
    <ul>    
        <li><strong>01단계</strong> 배열에서 두 수를 선택하는 모든 경우의 수를 구합니다.</li>
        <li><strong>02단계</strong> 과정 1에서 구한 수를 새로운 배열에 저장하고 중복값을 제거합니다.</li>
        <li><strong>03단계</strong> 배열을 오름차순으로 정렬하고 반환합니다.</li>
    </ul>
<p>배열에서 두 수를 선택하는 방법은 다음 그림처럼 각 수에서 자신보다 뒤에 있는 수를 선택하면 됩니다. 빠짐 없이 모든 두 수를 선택할 수 있습니다.</p>
<pre><code>
def solution(numbers):
    ret = [ ]  # 1. 빈 배열 생성
    # 2. 두 수를 선택하는 모든 경우의 수를 반복문으로 구함
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            # 3. 두 수를 더한 결과를 새로운 배열에 추가
            ret.append(numbers[i] + numbers[j])
    # 4. 중복된 값을 제거하고, 오름차순으로 정렬
    ret = sorted(set(ret))
    return ret  # 5. 최종 결과 반환 
</code></pre>
    <p>1. ret 배열은 최종 반환 배열입니다. 초기 상태이므로 아무 데이터도 없습니다.</p>
    <p>2. numbers의 데이터에서 두 수를 선택하는 동작을 구현한 코드입니다. 표를 보면 반복문의 의미를 쉽게 이해할 수 있습니다. i = 0, j = 2인 경우 {5, 2} => 7이라고 표시했습니다.</p>
    <p>3. 표와 같이 구한 합을 변수 ret에 append( ) 메서드로 리스트에 추가합니다. 중복값을 제거하기 전이므로 지금은 [5, 7, 12, 2, 7, 9]입니다.</p>
    <p>4. 이후 sorted( ) 함수로 중복값을 제거한 ret을 오름차순으로 정렬해 반환하면 문제 풀이는 끝입니다.</p>
    <h3 id="_4">시간 복잡도 분석하기</h3>
    <p>N은 lst의 길이입니다. lst의 중복 원소를 제거하는 데 걸리는 시간 복잡도는 O(N)이고, 이를 다시 정렬하는 데 걸리는 시간 복잡도는 O(NlogN)이므로 최종 시간 복잡도는 O(NlogN)입니다.</p>
</div>