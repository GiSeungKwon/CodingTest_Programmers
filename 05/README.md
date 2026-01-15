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
    <h1>문제 05 행렬의 곱셈★</h1>
    <p>정답률 _ 63% | 저자 권장 시간 _ 40분 | 권장 시간 복잡도 _ O(N3) | 출제 _ 연습문제</p>
    <p><a href="https://school.programmers.co.kr/learn/courses/30/lessons/12949" data-google-vignette="false">문제 URL</a></p>
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
                <th>입력</th>
                <th>출력</th>
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
    <p>가장 먼저 해야 할 일은 수포자들의 문제를 찍는 패턴을 분석하는 겁니다. 각 수포자가 문제를 찍는 패턴은 다음 그림과 같습니다.</p>
    <ul>    
        <li><strong>[1,2,3,4,5] 반복</strong></li>
        <li><strong>[2,1,2,3,2,4,2,5] 반복</strong></li>
        <li><strong>[3,3,1,1,2,2,4,4,5,5] 반복</strong></li>
    </ul>
<p>패턴을 찾았으므로 각 패턴으로 문제를 풀 경우 몇 개를 맞출 수 있는지 체크합니다. 문제 번호에 대해 수포자의 답과 실제 답이 일치할 때마다 점수를 획득하는데, 이 점수가 가장 큰 수포자를 찾습니다. 예를 들어 답이 [1, 4, 2, 4, 2]인 경우 수포자 1, 수포자 2는 2문제를 맞췄고, 수포자 3은 1문제를 맞춥니다. 이 경우 최대 점수를 얻은 수포자는 수포자 1과 수포자 2입니다.</p>
<p>만약 답이 [1, 3, 5, 7, 9, 2, 4, 5]이면 답의 길이가 8이고 수포자 1의 패턴 길이는 5이므로 답의 길이가 수포자 1의 패턴 길이보다 깁니다. 그런 경우 다음 그림과 같이 코드를 설계해야 합니다. 그림을 보면 [1, 3, 5, 7, 9]까지는 기존 방식으로 답안을 매치하면 되고 수포자 1과 같이 패턴 길이를 넘어서는 [2, 4, 5]는 수포자1의 답 패턴 첫 번째부터 매치하면 됩니다.</p>
<p>이렇게 하면 모든 수포자의 점수를 구할 수 있습니다. 가장 높은 점수를 획득한 수포자의 번호를 반환할 때 주의할 점은 동점 조건입니다. 수포자들이 얻은 점수의 최댓값을 먼저 구하고 이 점수와 일치하는 수포자의 번호를 오름차순으로 반환하면 동점 조건을 해결할 수 있습니다.</p>
<pre><code>
def solution(answers):
  # ➊ 수포자들의 패턴
  patterns = [
    [1, 2, 3, 4, 5], 
    [2, 1, 2, 3, 2, 4, 2, 5], 
    [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
  ] 
  # ➋ 수포자들의 점수를 저장할 리스트
  scores = [0] * 3    
  # ➌ 각 수포자의 패턴과 정답이 얼마나 일치하는지 확인
  for i, answer in enumerate(answers):
    for j, pattern in enumerate(patterns):
      if answer == pattern[i % len(pattern)]:
        scores[j] += 1  
  # ➍ 가장 높은 점수 저장
  max_score = max(scores)
  # ➎ 가장 높은 점수를 가진 수포자들의 번호를 찾아서 리스트에 담음
  highest_scores = [ ]
  for i, score in enumerate(scores):
    if score == max_score:
      highest_scores.append(i + 1)
  return highest_scores  
</code></pre>
    <p>➊ 수포자들의 패턴을 미리 리스트에 저장합니다. 이렇게 특정 패턴이 있으면 리스트에 미리 담아도 좋습니다. 이런 하드 코딩은 지양하는 것이 좋습니다만 적절하게 사용하면 효율이 좋아집니다.</p>
    <p>➋ 수포자들의 패턴과 답안을 비교해서 일치하는 개수를 저장하는 리스트를 선언했습니다. 이때 [0] * 3과 같은 기법은 [0, 0, 0]을 선언하는 것보다 간단해 자주 사용됩니다.</p>
    <p>➌ 정답과 수포자들의 패턴을 비교해서 각 수포자들의 점수를 구하는 부분입니다.</p>
    <p>반복문에서 in 연산자를 활용하는 형태가 좀 생소할 수 있습니다. 그림을 보며 반복문을 설명하겠습니다. 바깥쪽 반복문을 보면 i와 answer가 있습니다. i는 answer의 인덱스이고, answer는 해당 인덱스의 실젯값입니다. 이때 i는 0부터 증가합니다. 쉽게 말해 answers 리스트의 데이터를 0번부터 끝까지 반복하는 반복문입니다. 이렇게 리스트 전체를 반복해야 하는 경우 in 연산자를 활용하면 편리하게 반복문을 작성할 수 있습니다.</p>
    <p>바깥 반복문은 answers, 안쪽 반복문은 patterns의 데이터를 하나씩 가리킵니다. answer의 각 답안과 수포자들의 정답을 하나씩 비교하면서 정답이 일치하는 수포자의 경우 score를 1만큼 더합니다. 정답 패턴의 길이가 수포자의 답안 길이보다 긴 경우 정답 패턴의 처음 데이터와 다시 비교할 수 있도록 나머지 연산자를 사용했습니다.</p>
    <code>answer == pattern[i % len(pattern)]</code>
    <p>➍ 반복문에서 구한 각 수포자들의 점수 중 가장 큰 점수를 찾습니다. 동일 점수가 있을 수도 있으므로 일단 가장 큰 점수를 구하고 이 점수와 같은 수포자들을 찾는 방식을 구현합니다.</p>
    <p>➎ 가장 큰 점수를 갖는 수포자들을 찾아서 리스트에 담아 반환합니다.</p>
    <h3 id="_4">시간 복잡도 분석하기</h3>
    <p>N은 answers의 길이입니다. 각 수포자들의 패턴과 정답을 비교하는 부분은 O(N)입니다. 이후 scores를 순회하면서 가장 높은 점수를 받은 수포자를 추가하는 연산은 O(1)입니다. 따라서 최종 시간 복잡도는 O(N)입니다.</p>
</div>