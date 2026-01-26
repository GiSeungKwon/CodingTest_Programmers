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
    <h1>문제 13 크레인 인형 뽑기 게임★★</h1>
    <p>정답률 _ 51% | 저자 권장 시간 _ 60분 | 권장 시간 복잡도 _ O(N2 + M) 출제 _ 2019 카카오 개발자 겨울 인턴십</p>
    <p><a href="https://programmers.co.kr/learn/courses/30/lessons/64061" data-google-vignette="false">문제 URL</a></p>
    <hr>
    <p>게임 개발자인 죠르디는 크레인 인형 뽑기 기계를 모바일 게임으로 만들려고 합니다. 죠르디는 게임의 재미를 높이기 위해 화면 구성과 규칙을 다음과 같이 게임 로직에 반영하려고 합니다.</p>
    <img src="https://static.wikidocs.net/images/page/223107/06-3-13-1.png">
    <p>게임 화면은 1 × 1 크기의 격자로 구성된 N × N 크기의 격자이며 위쪽에는 크레인이 있고 오른쪽에는 바구니가 있습니다. 여러분이 보고 있는 화면은 5 × 5 크기의 격자 예입니다. 각 격자 칸에는 다양한 인형이 들어 있으며 인형이 없는 칸은 빈 칸입니다. 인형은 격자 한 칸을 차지하며 격자의 가장 아래 칸부터 차곡차곡 쌓입니다. 플레이어는 크레인을 좌우로 움직일 수 있고 크레인을 멈춘 위치에서 가장 위에 있는 인형을 집어 올릴 수 있습니다. 집어 올린 인형은 바구니에 쌓입니다. 이때 바구니의 가장 아래 칸부터 인형이 순서대로 쌓입니다. 다음은 ➊, ❷, ❸ [1번, 5번, 3번] 위치에서 순서대로 인형을 집어올려 바구니에 담은 모습입니다.</p>
    <img src="https://static.wikidocs.net/images/page/223107/06-3-13-2.png">
    <p>이 상태에서 ❹ 네모 인형이 1개 더 들어가면 어떻게 될까요? 같은 모양의 인형 2개가 바구니에 연속해 쌓이면 두 인형은 펑하고 터지며 사라집니다. 만약 인형이 없는 곳에서 크레인을 작동시키면 아무 일도 일어나지 않습니다. 또 바구니는 모든 인형이 들어갈 수 있을 만큼 충분히 큽니다. 2차원 배열 board와 인형을 집는 크레인을 작동시킨 위치가 담긴 배열 moves가 주어질 때, 크레인을 모두 작동시킨 후 사라진 인형 개수를 반환하는 solution( ) 함수를 완성하세요.</p>
    <img src="https://static.wikidocs.net/images/page/223107/06-3-13-3.png">
<!-- -->
    <h3>제약조건</h3>
    <ul>
        <li>board는 2차원 배열, 크기는 5 × 5 이상 30 × 30 이하입니다.</li>
        <li>board의 각 칸에는 0 이상 100 이하인 정수가 담겨 있습니다.</li>
        <ul>
            <li>0은 빈 칸을 나타냅니다.</li>
            <li>1 ~ 100의 각 숫자는 각기 다른 인형의 모양을 의미하며 같은 숫자는 같은 모양의 인형을 나타냅니다.</li>
        </ul>
        <li>moves 배열 크기는 1 이상 1,000 이하입니다.</li>
        <li>moves 배열 각 원소들의 값은 1 이상이며 board 배열의 가로 크기 이하인 자연수입니다.</li>
    </ul>
<!-- -->
    <h3>입출력의 예</h3>
    <table class="result-table">
        <thead>
            <tr>
                <th>board</th>
                <th>moves</th>
                <th>result</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>[[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]</td>
                <td>[1,5,3,5,1,2,1,4]</td>
                <td>4</td>
            </tr>
        </tbody>
    </table>
    <p>위와 같이 입출력이 주어지면 크레인이 [1, 5, 3, 5, 1, 2, 1, 4]번 위치에서 차례대로 인형을 집어서 바구니에 옮겨 담고, 최종으로 다음과 같은 상태가 됩니다.</p>
    <img src="https://static.wikidocs.net/images/page/223107/06-3-13-5.png">