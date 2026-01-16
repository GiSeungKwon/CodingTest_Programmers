<style>
    .result-table {
        border-collapse: collapse;
        width: 100%;
        max-width: 1000px;
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
        width: 33.33%;
    }
</style>

<div class="page-content tex2jax_process">
    <h1>문제 09 10진수를 2진수로 변환하기★</h1>
    <p>저자 권장 시간 _ 30분 | 권장 시간 복잡도 _ O(logN) | 출제 _ 저자 출제</p>
    <p><a href="https://github.com/dremdeveloper/codingtest_python/blob/main/solution/09.py" data-google-vignette="false">문제 URL</a></p>
    <hr>
    <p>10진수를 입력받아 2진수로 변환해 반환하는 solution( ) 함수를 구현하세요.</p>
    <!-- -->
    <h3>제약조건</h3>
    <ul>
        <li>제약 조건 없음</li>
    </ul>
    <h3>입출력의 예</h3>
    <table class="result-table">
        <thead>
            <tr>
                <th>decimal</th>
                <th>반환값</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>10</td>
                <td>1010</td>
            </tr>
            <tr>
                <td>27</td>
                <td>11011</td>
            </tr>
            <tr>
                <td>12345</td>
                <td>11000000111001</td>
            </tr>
        </tbody>
    </table>
    <!-- -->
    <h3>문제 분석하고 풀기</h3>
    <p>우선 10진수를 2진수로 표현하는 과정을 봅시다. 10진수를 2진수로 표현하는 과정은 다음과 같으며, 이 과정은 이미 수학적으로 증명된 것이므로 별도로 설명하지 않겠습니다.</p>
    <p>1 10진수 N을 2로 나눈 나머지, 즉, %2 연산을 한 값을 저장하고, N은 2로 나눔</p>
    <p>2 몫이 0이 아니라면 나머지를 버리고 다시 1을 수행</p>
    <p>3 모든 과정이 끝나고 1에서 저장한 수를 뒤부터 순서대로 가져와 붙이기</p>
    <h3>십진수를 2진수로 변환하는 과정</h3>
    <p>십진수 13을 위 과정대로 변경하는 모습은 다음과 같습니다. 13을 2로 나누면서 나눈 나머지를 순서대로 저장합니다. 이 과정을 0이 될 때까지 반복합니다. 몫이 0이 되면 저장한 값을 뒤부터 순서대로 읽으면 1101으로 이진수 변환이 완료됩니다.</p>
<pre><code>
def solution(s):
  stack = [ ]
  for c in s:
    if c == "(":
      stack.append(c)
    elif c == ")":
      if not stack:
        return False
      else:
        stack.pop( ) 
  if stack:
    return False
  else:
    return True
</code></pre>
    
<!-- -->
<h3 id="_4">시간 복잡도 분석하기</h3>
<p>N은 s의 길이입니다. s를 순회하며 괄호의 쌍을 확인하므로 시간 복잡도는 O(N)입니다. 참고로 괄호 쌍을 확인할 때 append( ) 메서드와 pop( ) 메서드의 시간 복잡도는 O(1)입니다.</p>
</div>