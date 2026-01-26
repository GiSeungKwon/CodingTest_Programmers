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
