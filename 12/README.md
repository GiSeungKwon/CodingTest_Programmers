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
    <h1>문제 12 주식 가격★★</h1>
    <p>정답률 _ 57% | 저자 권장 시간 _ 40분 | 권장 시간 복잡도 _ O(N) | 출제 _ 스택/큐</p>
    <p><a href="https://programmers.co.kr/learn/courses/30/lessons/42584" data-google-vignette="false">문제 URL</a></p>
    <hr>
    <p>초 단위로 기록된 주식 가격이 담긴 배열 prices가 매개변수로 주어질 때, 가격이 떨어지지 않은 기간은 몇 초인지를 반환하도록 solution( ) 함수를 완성하세요.</p>
<!-- -->
    <h3>제약조건</h3>
    <ul>
        <li>prices의 각 가격은 1 이상 10,000 이하인 자연수입니다.</li>
        <li>prices의 길이는 2 이상 100,000 이하입니다.</li>
    </ul>
<!-- -->
    <h3>입출력의 예</h3>
    <table class="result-table">
        <thead>
            <tr>
                <th>prices</th>
                <th>return</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>[1,2,3,2,3]</td>
                <td>[4,3,1,1,0]</td>
            </tr>
        </tbody>
    </table>
    <!-- -->
    <h3>문제 분석하고 풀기</h3>
    <p>문자열 문제를 처음 보는 많은 사람이 이중 반복문으로 문제를 해결하려는 경우가 많습니다. 하지만 우리는 문자열의 길이를 봐야 합니다. 문자열의 길이는 최대 100만이므로 이중 반복문, 즉, 시간 복잡도가 O(N2)인 알고리즘으로 접근하면 무조건 시간 초과가 발생합니다. 이 문제는 시간 복잡도가 O(N)인 알고리즘을 적용해야 합니다.</p>
    <h3>문자열 제거 과정 생각해보기</h3>
    <p>슬프게도 이 문제도 바로 스택을 떠올리기 쉽지 않습니다. 정답 코드를 보면 알겠지만 코드는 굉장히 간단합니다. 알고리즘을 떠올리기 어려울 뿐이죠. 이 문제의 정답률이 굉장히 낮은 이유입니다. 앞서 이야기한 것처럼 알고리즘이 바로 떠오르지 않으면 일단 문제를 이해하고 간단한 입력값, 출력값으로 문제가 해결되는 과정을 직접 그려보는 것이 좋습니다.</p>
    <h3>01단계 다음과 같이 문자열이 있다고 생각해봅시다.</h3>
    <img src="https://static.wikidocs.net/images/page/223105/06-3-11-2.png">
    <h3>02단계 그러면 가장 왼쪽부터 탐색해 AA를 찾아 제거합니다.</h3>
    <img src="https://static.wikidocs.net/images/page/223105/06-3-11-3.png">
    <h3>03단계 문자열을 제거한 다음에는 BB가 붙으므로 BB를 제거하고, 이어서 AA를 제거합니다.</h3>
    <img src="https://static.wikidocs.net/images/page/223105/06-3-11-4.png">
    <h3>04단계 이 과정을 모두 마치면 모든 문자열이 제거되므로 이 문자열은 짝이 맞습니다.</h3>
    <p>이제 두 문자가 만나서 문자를 삭제하고, 붙이는 과정을 수학적으로 접근해봅시다. 현재 가리키고 있는 문자가 i번째면 다음 문자는 i + 1번째이므로 이 둘을 비교합니다. 이를 거꾸로 생각해 i + 1번째 문자 입장으로 이야기하면 바로 직전 문자, 즉, 최근 문자와 비교한다고 생각할 수 있습니다. 좀 더 그럴듯하게 말해서 가장 최근에 탐색한 데이터를 먼저 비교한다고 할 수 있겠네요. 이는 스택의 구조와 맞아 떨어집니다. 그리고 문제 요구사항인 짝이 맞는 문자를 제거한 다음 문자열을 붙이는 연산은 팝 연산으로 자연스럽게 해결할 수 있으므로 구현 시 고려할 필요가 없습니다. 이 내용은 코드 작성 후 다시 설명하겠습니다.</p>
    <p>처음에는 이런 생각이 쉽게 들지 않을 겁니다. 필자도 온종일 생각해도 문제를 풀 방법이 떠오르지 않았던 때가 있습니다. 그럴 때는 더 시간을 쏟지 말고 정답을 보는 것도 방법입니다. 다만 정답을 본 후에 정답에 적용한 알고리즘이 어떻게 나온 것인지 생각하는 시간을 꼭 가져보세요.</p>
    <p>그럼 코드로 구현해봅시다. 앞서 언급했듯이 스택을 사용한 아주 간단한 코드입니다.</p>    
<pre><code>
def solution(s):
  stack = [ ]  # 스택 초기화
  for c in s:
    if stack and stack[-1] == c:  # ➊ 스택이 비어 있지 않고, 
       # 현재 문자와 스택의 맨 위 문자가 같으면
      stack.pop( )   # ➋ 스택의 맨 위 문자 제거
    else:
      stack.append(c)    # ➌ 스택에 현재 문자 추가
  return int(not stack)  # ➍ 스택이 비어 있으면 1, 그렇지 않으면 0 반환 
</code></pre>
<!-- -->
<p>사실 실제 문자열을 이어붙일 필요는 없습니다. 문제의 핵심은 문자열의 짝을 전부 제거할 수 있는지 체크하는 겁니다. 이 부분을 충분히 고려하면서 실제 구현된 코드를 해석하겠습니다.</p>
<ul>
    <li>➊ 구현 시 많이 실수하는 부분입니다. stack[-1]은 stack의 top, 즉, 이 위치에는 최근에 추가한 데이터가 있습니다. 다만 스택이 빈 경우도 고려해야 하므로 top 위치의 원소값부터 체크하지 말고 반드시 stack이 비었는지 체크해야 합니다. 스택 문제에서 많이 실수하는 부분입니다. 스택이 빈 경우를 항상 고려하기 바랍니다.</li>
    <li>➋ 현재 문자 c와 최근 원소의 문자가 같다면 팝합니다. </li>
    <li>➌ 스택에 원소가 없다면 푸시합니다. </li>
    <li>➍ 모든 문자열을 순회했을 때 스택이 비어 있다면 짝지어 제거하기가 완료된 겁니다. 따라서 스택이 비어 있으면 1을, 그렇지 않으면 0을 반환합니다.</li>
</ul>
<!-- -->
<h3 id="_4">시간 복잡도 분석하기</h3>
<p>N은 s의 길이입니다. 문자열의 모든 문자를 한 번씩 순회하므로 시간 복잡도는 O(N)입니다.</p>
</div>