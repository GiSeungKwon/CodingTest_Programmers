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
    <h1>문제 04 모의고사★</h1>
    <p>정답률 _ 62% | 저자 권장 시간 _ 30분 | 권장 시간 복잡도 _ O(N) | 출제 _ 완전 탐색</p>
    <a href="https://programmers.co.kr/learn/courses/30/lessons/42840" data-google-vignette="false">문제 URL</a>
    <hr>
    <p>수포자는 수학을 포기한 사람을 줄인 표현입니다. 수포자 삼인방은 모의고사에 수학 문제를 전부 찍으려 합니다. 수포자는 1번 문제부터 마지막 문제까지 다음과 같이 찍습니다.</p>
    <ul>
        <li>1번 수포자가 찍는 방식 : 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, ...</li>
        <li>2번 수포자가 찍는 방식 : 2, 1, 2, 3, 2, 4, 2, 5, 2, 1, 2, 3, 2, 4, 2, 5, ...</li>
        <li>3번 수포자가 찍는 방식 : 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, ...</li>
    </ul>
    <p>1번 문제부터 마지막 문제까지의 정답이 순서대로 저장된 배열 answers가 주어졌을 때 가장 많은 문제를 맞힌 사람이 누구인지 배열에 담아 반환하도록 solution( ) 함수를 작성하세요.</p>
    <h3 id="_1">제약조건</h3>
    <ul>
        <li>시험은 최대 10,000 문제로 구성되어 있습니다.</li>
        <li>문제의 정답은 1, 2, 3, 4, 5 중 하나입니다.</li>
        <li>가장 높은 점수를 받은 사람이 여럿이라면 반환하는 값을 오름차순으로 정렬하세요.</li>
    </ul>
    <h3 id="_2">입출력의 예</h3>
    <table class="result-table">
        <thead>
            <tr>
                <th>answers</th>
                <th>return</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>[1,2,3,4,5]</td>
                <td>[1]</td>
            </tr>
            <tr>
                <td>[1,3,2,4,2]</td>
                <td>[1,2,3]</td>
            </tr>
        </tbody>
    </table>
    <h3 id="_3">문제 분석하고 풀기</h3>
    <p></p>
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
    <p>N은 numbers의 길이입니다. 모든 조합을 확인하는 과정에서 중복을 체크하는 데 O(N2)이 걸립니다. 그리고 이를 정렬하는 데 O(N2log(N2))이 걸리므로 최종 시간 복잡도는 O(N2log(N2))입니다. 다만 N = 100이므로 시간 복잡도를 이렇게 해도 문제를 푸는 데는 크게 영향이 없습니다.</p>
</div>