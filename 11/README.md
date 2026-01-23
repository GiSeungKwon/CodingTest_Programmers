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
    <h1>문제 11 짝지어 제거하기★</h1>
    <p>정답률 _ 71% | 저자 권장 시간 _ 30분 | 권장 시간 복잡도 _ O(N) | 출제 _ 2017 팁스타운</p>
    <p><a href="https://programmers.co.kr/learn/courses/30/lessons/12973" data-google-vignette="false">문제 URL</a></p>
    <hr>
    <p>알파벳 소문자로 구성된 문자열에서 같은 알파벳이 2개 붙어 있는 짝을 찾습니다. 짝을 찾은 다음에는 그 둘을 제거한 뒤 앞뒤로 문자열을 이어붙입니다. 이 과정을 반복해서 문자열을 모두 제거한다면 짝지어 제거하기가 종료됩니다. 문자열 S가 주어졌을 때 짝지어 제거하기를 성공적으로 수행할 수 있는지 반환하는 함수를 완성하세요. 성공적으로 수행할 수 있으면 1을, 아니면 0을 반환해주면 됩니다. 예를 들어 문자열 S가 baabaa라면</p>
    <ul><li>baabaa → bbaa → aa</li></ul>
    <p>순서로 문자열을 모두 제거할 수 있으므로 1을 반환합니다.</p>
<!-- -->
    <h3>제약조건</h3>
    <ul>
        <li>문자열의 길이 : 1,000,000 이하의 자연수</li>
        <li>문자열은 모두 소문자로 이루어져 있습니다.</li>
    </ul>
<!-- -->
    <h3>입출력의 예</h3>
    <table class="result-table">
        <thead>
            <tr>
                <th>s</th>
                <th>result</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>"baabaa"</td>
                <td>1</td>
            </tr>
            <tr>
                <td>"cdcd"</td>
                <td>0</td>
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
    <img src="https://static.wikidocs.net/images/page/223101/06-3-09-2.png">
    <p>이 문제도 스택으로 쉽게 풀 수 있습니다. 스택에 저장할 데이터가 무엇인지 정의하면 됩니다. 그림의 왼쪽을 보면 10진수 N을 2로 나누며 나머지를 표시했는데 이 나머지를 거꾸로 읽으면 우리가 원하는 이진수가 됩니다. 즉, 나머지를 스택에 쌓고, 하나씩 꺼내면 답이 나옵니다.</p>
    <p>01단계 다음 그림을 보며 이해해봅시다. 초기에는 13으로 시작합니다. 이것을 2로 나누고 나머지를 스택에 푸시합니다. 13을 2로 나눈 나머지가 1이므로 1을 푸시했습니다.</p>
    <img src="https://static.wikidocs.net/images/page/223101/06-3-09-3.png">
    <p>02단계 그다음도 같은 작업을 계속합니다. 6을 2로 나눈 나머지는 0이므로 0을 푸시하고, 3을 2로 나눈 나머지는 1이므로 1을 푸시합니다.</p>
    <img src="https://static.wikidocs.net/images/page/223101/06-3-09-4.png">
    <p>03단계 십진수 13을 몫이 0이 될 때까지 나눈 결과로 스택에는 1, 0, 1, 1이 쌓였습니다.</p>
    <img src="https://static.wikidocs.net/images/page/223101/06-3-09-5.png">
    <p>04단계 연산이 끝난 후 스택에서 팝한 값을 나열하면 13을 이진수로 변환한 1101이 됩니다.</p>
    <img src="https://static.wikidocs.net/images/page/223101/06-3-09-6.png">
    <p>지금까지 설명한 내용을 바탕으로 코드를 작성하면 다음과 같습니다.</p>
<pre><code>
def solution(decimal):
  stack = [ ]
  while decimal > 0:
    remainder = decimal % 2
    stack.append(str(remainder))
    decimal //= 2
  binary = ""
  while stack:
    binary += stack.pop( ) 
# 이 문제에서는 스택 활용을 보여주기 위해 pop()을 했지만 문자열에 계속해서 문자를 더할 때는 join() 메서드가 더 효율적입니다.
  return binary
</code></pre>
    
<!-- -->
<h3 id="_4">시간 복잡도 분석하기</h3>
<p>N은 이진수로 변환할 숫자입니다. N을 이진수로 변환하는 과정은 N이 1이 될 때까지 2로 계속 나누므로 연산 횟수는 O(logN)입니다. 하지만 문자열의 += 연산자는 수행할 때마다 객체를 새로 생성합니다. 따라서 시간 복잡도는 O((logN)2)이 됩니다.</p>
<p>join( ) 메서드를 활용하면 시간 복잡도를 O(logN)으로 낮출 수 있습니다.</p>
</div>