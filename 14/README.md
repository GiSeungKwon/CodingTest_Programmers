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
    <h1>문제 14 표 편집★★★★</h1>
    <p>정답률 _ 36% | 저자 권장 시간 _ 80분 | 권장 시간 복잡도 _ O(N)
출제 _ 2021 카카오 채택연계형 인턴십</p>
    <p><a href="https://programmers.co.kr/learn/courses/30/lessons/81303" data-google-vignette="false">문제 URL</a></p>
    <hr>
    <p>업무용 소프트웨어를 개발하는 니니즈웍스의 인턴인 앙몬드는 명령어 기반으로 표의 행을 선택, 삭제, 복구하는 프로그램을 작성하는 과제를 맡았습니다. 세부 요구사항은 다음과 같습니다.</p>
    <img src="https://static.wikidocs.net/images/page/223108/06-3-14-1.png">
    <p>표에서 진하게 칠한 칸은 선택한 행입니다. 한 번에 한 행만 선택할 수 있으며 표의 범위를 벗어날 수 없습니다. 이때 다음과 같은 명령어를 이용해 표를 편집합니다.</p>
    <ul>
        <li>“U X” : 현재 선택한 행에서 X칸 위에 있는 행을 선택합니다.</li>
        <li>“D X” : 현재 선택한 행에서 X칸 아래에 있는 행을 선택합니다.</li>
        <li>“C” : 현재 선택한 행을 삭제한 후, 바로 아래 행을 선택합니다. 단, 삭제된 행이 가장 마지막 행인 경우 바로 윗 행을 선택합니다.</li>
        <li>“Z” : 가장 최근에 삭제한 행을 원래대로 복구합니다. 단, 현재 선택한 </li>행은 바뀌지 않습니다.</li>
    </ul>
    <p>예를 들어 위 표에서 “D 2”를 수행하면 다음 그림의 왼쪽처럼 4행이 선택되며 “C”를 수행하면 선택된 행을 삭제하고 바로 아래 행이었던 “네오”가 적힌 행을 선택합니다.</p>
    <img src="https://static.wikidocs.net/images/page/223108/06-3-14-2.png">
    <p>다시 “U 3”을 수행한 다음 “C”를 수행한 후의 표 상태는 다음 그림과 같습니다.</p>
    <img src="https://static.wikidocs.net/images/page/223108/06-3-14-3.png">
    <p>다음으로 “D 4”를 수행한 다음 “C”를 수행한 후의 표 상태는 다음 그림과 같습니다. 5행이 표의 마지막 행이므로, 이 경우 바로 윗 행을 선택하는 점에 주의합니다.</p>
    <img src="https://static.wikidocs.net/images/page/223108/06-3-14-4.png">
    <p>“U 2”를 수행하면 현재 선택한 행은 2행이 됩니다.</p>
    <img src="https://static.wikidocs.net/images/page/223108/06-3-14-5.png">
    <p>위 상태에서 “Z”를 수행하면 가장 최근에 제거한 “라이언”이 적힌 행이 복구됩니다.</p>
    <img src="https://static.wikidocs.net/images/page/223108/06-3-14-6.png">
    <p>다시 한번 “Z”를 수행하면 그다음으로 제거한 “콘”이 적힌 행이 복구됩니다. 현재 선택된 행은 바뀌지 않는 점에 주의하세요.</p>
    <img src="https://static.wikidocs.net/images/page/223108/06-3-14-7.png">
    <p>최종 표의 상태와 처음 표의 상태를 비교해 삭제되지 않은 행은 “O”, 삭제된 행은 “X”로 표시하면 다음과 같습니다.</p>
    <img src="https://static.wikidocs.net/images/page/223108/06-3-14-8.png">
    <p>처음 표의 행 개수를 나타내는 정수 n, 처음에 선택한 행의 위치를 나타내는 정수 k, 수행한 명령어들이 담긴 문자열 배열 cmd가 주어질 때, 모든 명령어를 수행한 후의 표의 상태와 처음 표의 상태를 비교해 삭제되지 않은 행은 O, 삭제된 행은 X로 표시해 문자열 형태로 반환하는 solution( ) 함수를 완성하세요.</p>
<!-- -->
    <h3>제약조건</h3>
    <ul>
        <li>5 ≤ n ≤ 1,000,000</li>
        <li>0 ≤ k < n</li>
        <li>1 ≤ cmd의 원소 개수 ≤ 200,000</li>
        <li>cmd의 각 원소는 “U X”, “D X”, “C”, “Z” 중 하나입니다.</li>
        <li>X는 1 이상 300,000 이하인 자연수이며 0으로 시작하지 않습니다.</li>
        <li>X가 나타내는 자연수에 쉼표는 없습니다. 예를 들어 123,456가 아니라 123456와 같이 자연수가 주어집니다.</li>
        <li>cmd에 등장하는 모든 X들의 값을 합친 결과가 1,000,000 이하인 경우만 입력으로 주어집니다.</li>
        <li>표의 모든 행을 제거해 행이 하나도 남지 않는 경우는 입력으로 주어지지 않습니다.</li>
        <li>문제에서 각 행이 제거되고 복구되는 과정을 자연스럽게 보여주기 위해 “이름”이라는 열을 사용했으나, 실제 문제를 푸는 과정에는 필요하지 않습니다. “이름” 열에는 서로 다른 이름들이 중복 없이 채워져 있다고 가정하고 문제를 해결하세요.</li>
        <li>표의 범위를 벗어나는 이동은 입력으로 주어지지 않습니다.</li>
        <li>원래대로 복구할 행이 없을 때, 즉, 삭제한 행이 없을 때 “Z”가 명령어로 주어지는 경우는 없습니다.</li>
        <li>정답은 표의 0행부터 n - 1행까지에 해당되는 O, X를 순서대로 이어붙인 문자열 형태로 반환해주세요.</li>
    </ul>
    <h3>정확성 테스트 케이스 제약 조건</h3>
    <ul>
        <li>정확성 테스트 : 10초</li>
        <li>5 ≤ n ≤ 1,000</li>
        <li>1 ≤ cmd의 원소 개수 ≤ 1,000</li>
    </ul>
    <h3>효율성 테스트 케이스 제약 조건</h3>
    <ul>
        <li>효율성 테스트 : 언어별로 작성된 정답 코드의 실행 시간의 적정 배수</li>
        <li>주어진 조건 외 추가 제약 조건 없습니다.</li>
    </ul>
<!-- -->
    <h3>입출력의 예</h3>
    <table class="result-table">
        <thead>
            <tr>
                <th>n</th>
                <th>k</th>
                <th>cmd</th>
                <th>result</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>8</td>
                <td>2</td>
                <td>["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]</td>
                <td>"OOOOXOOO"</td>
            </tr>
            <tr>
                <td>8</td>
                <td>2</td>
                <td>["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]</td>
                <td>"OOXOXOOO"</td>
            </tr>
        </tbody>
    </table>