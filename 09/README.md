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
    <h1>문제 08 괄호 짝 맞추기★★</h1>
    <p>저자 권장 시간 _ 30분 | 권장 시간 복잡도 _ O(N) | 출제 _ 저자 출제</p>
    <p><a href="https://github.com/dremdeveloper/codingtest_python/blob/main/solution/08.py" data-google-vignette="false">문제 URL</a></p>
    <hr>
    <p>소괄호는 짝을 맞춘 열린 괄호 ‘(’와 닫힌 괄호 ‘)’로 구성합니다. 문제에서는 열린 괄호나 닫힌 괄호가 마구 뒤섞인 문자열을 줍니다. 이때 소괄호가 정상으로 열고 닫혔는지 판별하는 solution( ) 함수를 구현하세요. 만약 소괄호가 정상적으로 열고 닫혔다면 True를, 그렇지 않다면 False를 반환하면 됩니다.</p>
    <!-- -->
    <h3>제약조건</h3>
    <ul>
        <li>열린 괄호는 자신과 가장 가까운 닫힌 괄호를 만나면 상쇄됩니다.</li>
        <li>상쇄 조건은 열린 괄호가 먼저 와야 하고, 열린 괄호와 닫힌 괄호 사이에 아무것도 없어야 합니다.</li>
        <li>더 상쇄할 괄호가 없을 때까지 상쇄를 반복합니다.</li>
    </ul>
    <h3>입출력의 예</h3>
    <table class="result-table">
        <thead>
            <tr>
                <th>s</th>
                <th>반환값</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>( () ) ()</td>
                <td>True</td>
            </tr>
            <tr>
                <td>(( () ) ()</td>
                <td>False</td>
            </tr>
        </tbody>
    </table>
    <!-- -->
    <h3 id="_3">문제 분석하고 풀기</h3>
    <p>이런 괄호 짝 맞추기를 해결하려면 어떻게 해야 할까요? 바로 스택을 사용하면 됩니다. 스택을 어떻게 적용할 수 있는지 알아보겠습니다. 여러분이 문제 조건에서 주목해야 할 내용은 닫힌 괄호가 임의 위치의 열린 괄호와 상쇄되는 것이 아니라 닫힌 괄호가 나오기 바로 전의, 즉, 가장 가까운(최근) 열린 괄호와 상쇄된다는 겁니다. 가장 가까운(최근)이라는 키워드를 보고 스택을 떠올리는 감각이 있어야 합니다. 스택과 함께 이 문제를 풀려면 다음과 같은 과정으로 괄호를 상쇄하면 됩니다.</p>
    <p>1 문자열을 앞에서 하나씩 보며 열린 괄호가 나오면 푸시</p>
    <p>2 닫힌 괄호가 나오면 팝 연산을 통해 문자열에서 열린 괄호, 닫힌 괄호 한 쌍을 상쇄</p>
    <p>3 1~2를 마지막 문자열까지 반복해 스택에 열린 괄호가 남아 있다면 짝이 맞지 않은 것(False)이고, 괄호가 남아 있지 않다면 짝이 맞은 것(True)으로 판단</p>
    <p>실제 데이터와 함께 위 과정을 연습해봅시다.</p>
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