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
    <h1>문제 07 방문 길이★★</h1>
    <p>정답률 _ 57% | 저자 권장 시간 _ 40분 | 권장 시간 복잡도 _ O(N) 출제 _ Summer/Winter Coding(~2018)</p>
    <p><a href="https://school.programmers.co.kr/learn/courses/30/lessons/49994" data-google-vignette="false">문제 URL</a></p>
    <hr>
    <p>게임 캐릭터를 4가지 명령어를 통해 움직이려 합니다. 명령어는 다음과 같습니다.</p>
    <ul>
        <li>U : 위쪽으로 한 칸 가기</li>
        <li>D : 아래쪽으로 한 칸 가기</li>
        <li>R : 오른쪽으로 한 칸 가기</li>
        <li>L : 왼쪽으로 한 칸 가기</li>
    </ul>
    <p>캐릭터는 좌표평면의 (0, 0) 위치에서 시작합니다. 좌표평면의 경계는 왼쪽 위(-5, 5), 왼쪽 아래(-5, -5), 오른쪽 위(5, 5), 오른쪽 아래(5, -5)로 구성합니다.</p>
    <img src="https://static.wikidocs.net/images/page/223089/05-5-07-1.png">
    <p>예를 들어 ULURRDLLU라고 명령하면 ➊~➐까지는 이렇게 움직입니다.</p>
    <img src="https://static.wikidocs.net/images/page/223089/05-5-07-2.png">
    <p>➑~➒까지는 다음과 같이 움직입니다.</p>
    <img src="https://static.wikidocs.net/images/page/223089/05-5-07-3.png">
    <p>이때 우리는 게임 캐릭터가 지나간 길 중 캐릭터가 처음 걸어본 길의 길이를 구하려고 합니다. 예를 들어 위의 예시에서 게임 캐릭터가 움직인 길이는 9이지만 캐릭터가 처음 걸어본 길의 길이는 7이 됩니다. 다시 말해 8, 9번 명령어에서 움직인 길은 2, 3번 명령어에서 이미 거쳐간 길입니다. 그리고 좌표평면의 경계를 넘어가는 명령어는 무시합니다. 예를 들어 LULLLLLLU로 명령하면 ➊~➏ 명령어대로 움직이고 ➐~➑ 명령어는 무시합니다. 그리고 다시 ➒ 명령어대로 움직입니다.</p>
    <img src="https://static.wikidocs.net/images/page/223089/05-5-07-4.png">
    <p>이때는 캐릭터가 처음 걸어본 길의 길이는 7이 됩니다. 명령어가 매개변수 dirs로 주어질 때 게임 캐릭터가 처음 걸어본 길의 길이를 구해 반환하는 solution( ) 함수를 완성하세요.</p>
    <h3 id="_1">제약조건</h3>
    <ul>
        <li>dirs는 string형으로 주어지며, ‘U’, ‘D’, ‘R’, ‘L’ 이외의 문자는 주어지지 않습니다.</li>
        <li>dirs의 길이는 500 이하의 자연수입니다.</li>
    </ul>
    <h3 id="_2">입출력의 예</h3>
    <table class="result-table">
        <thead>
            <tr>
                <th>dirs</th>
                <th>answer</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>ULURRDLLU</td>
                <td>7</td>
            </tr>
            <tr>
                <td>LULLLLLLU</td>
                <td>7</td>
            </tr>
        </tbody>
    </table>
    <!-- -->
    <h3 id="_3">문제 분석하고 풀기</h3>
    <p>이 문제는 명령어 대로 로봇이 이동할 때 중복 경로의 길이를 제외한 움직인 경로의 길이를 반환해야 합니다. 이 문제의 경우 문제 자체가 복잡하진 않지만 구현 시 실수하기가 쉽습니다. 어디에서 실수하기 쉬울까요?</p>
    <p>첫 번째, 중복 경로는 최종 길이에 포함하지 않는다는 조건입니다. 이부분을 어떻게 처리할지 충분히 고민해야 합니다. 중복을 포함하지 않는다는 문장이 나오면 set( ) 함수를 생각해보면 좋습니다. 언급했던 것처럼 중복 처리를 직접하는 것보다 괜찮습니다.</p>
    <p>두 번째, 음수 좌표를 포함한다는 점입니다. 문제를 보면 좌표 범위는 -5 <= x, y <= 5입니다. 2차원 배열에서 음수 인덱스를 사용할 수는 없으므로 다른 방법을 생각해야 합니다. 문제의 핵심은 원점에서 출발해 최종 경로의 길이를 구하는 건데, 좌표는 방향에 의해서만 제어된다는 점입니다. 따라서 원점을 (0, 0)에서 (5, 5)로 바꿔 음수 좌표 문제를 해결해도 됩니다. 이 문제는 구현 문제이므로 별다른 알고리즘 설명은 필요하지 않습니다. 다른 알고리즘 문제도 마찬가지지만 구현 문제는 답안 코드의 길이가 긴 경우가 많으므로 기능별로 함수를 구현하는 게 좋습니다. 처음부터 기능별 구현이 잘 될 수는 없습니다. 그럴 때는 일단 하나의 함수로 전체 동작을 구현해보고 이후 함수로 나누는 연습을 해보기 바랍니다.</p>
    <img src="https://static.wikidocs.net/images/page/223089/05-5-07-6.png">
    <p>위 2개를 해결했다면 이제 명령어에 따라 좌표의 경로를 추가한 뒤 중복 경로를 제거한 최종 이동 길이를 반환하면 됩니다.</p>
<pre><code>
def is_valid_move(nx, ny) : # ➊ 좌표평면을 벗어나는지 체크하는 함수
  return 0 <= nx < 11 and 0 <= ny < 11

def update_location(x, y, dir) : # ➋ 명령어를 통해 다음 좌표 결정
  if dir == 'U':
    nx, ny = x, y + 1
  elif dir == 'D':
    nx, ny = x, y - 1
  elif dir == 'L':
    nx, ny = x - 1, y
  elif dir == 'R':
    nx, ny = x + 1, y
  return nx, ny

def solution(dirs):
  x, y = 5, 5
  ans = set( ) # ➌ 겹치는 좌표는 1개로 처리하기 위함
  for dir in dirs : # ➍ 주어진 명령어로 움직이면서 좌표 저장
    nx, ny = update_location(x, y, dir)
    if not is_valid_move(nx, ny) : # ➎ 벗어난 좌표는 인정하지 않음
      continue
    # ➏ A에서 B로 간 경우 B에서 A도 추가해야 함(총 경로의 개수는 방향성이 없음)
    ans.add((x, y, nx, ny))
    ans.add((nx, ny, x, y))
    x, y = nx, ny # ➐ 좌표를 이동했으므로 업데이트
  return len(ans)/2 
</code></pre>
    <!-- -->
    <p>➊ 좌표가 주어진 범위를 초과했는지 체크하는 함수입니다. 해당 함수는 좌표 문제에 단골로 등장합니다. 핵심 알고리즘이랑 분리해 가독성을 높였습니다.</p>
    <p>➋ 현재 좌표와 방향을 받아 그다음 좌표를 반환하는 함수입니다.</p>
    <p>➌ 중복 좌표를 처리하기 위해 ans는 셋으로 정의합니다.</p>
    <p>➍ 주어진 명령어 순서대로 순회하는 코드입니다.</p>
    <p>➎ 주어진 명령어를 기준으로 다음 좌표를 구하고 해당 좌표가 유효한지 체크합니다. 유효하지 않으면 answer에 좌표를 추가하지 않습니다.</p>
    <p>➏ add((x, y, nx, ny))는 (x, y)에서 (nx, ny)까지의 경로를 방문했다라고 기록하는 것을 의미합니다. 이때 (x, y)에서 (nx, ny)만 저장하는 것이 아니라 그 반대인 (nx, ny)에서 (x, y) 역시 추가하는데 이 부분을 이해해야 코드를 제대로 이해한 것이라 할 수 있습니다.</p>
    <p>➐ 현재 좌표를 업데이트합니다.</p>
    <p>다음 그림을 보며 이해해봅시다. A→ B와 B→ A는 이 문제에서는 같은 경로로 취급합니다. 따라서 A→ B인 경우 A→ B와 B→ A를 둘 다 추가하고 나중에 최종 이동 길이를 2로 나눕니다.</p>
    <img src="https://static.wikidocs.net/images/page/223089/05-5-07-7.png">
    <!-- -->
    <h3 id="_4">시간 복잡도 분석하기</h3>
    <p>N은 dirs의 길이입니다. dirs의 길이만큼 순회하므로 시간 복잡도는 O(N)입니다.</p>
</div>