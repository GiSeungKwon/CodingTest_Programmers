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
    <h1>문제 05 행렬의 곱셈★</h1>
    <p>정답률 _ 63% | 저자 권장 시간 _ 40분 | 권장 시간 복잡도 _ O(N3) | 출제 _ 연습문제</p>
    <p><a href="https://school.programmers.co.kr/learn/courses/30/lessons/12949" data-google-vignette="false">문제 URL</a></p>
    <hr>
    <p>2차원 행렬 arr1과 arr2를 입력받아 arr1에 arr2를 곱한 결과를 반환하는 solution( ) 함수를 완성하세요.</p>
    <h3 id="_1">제약조건</h3>
    <ul>
        <li>행렬 arr1, arr2의 행과 열의 길이는 2 이상 100 이하입니다.</li>
        <li>행렬 arr1, arr2의 데이터는 -10 이상 20 이하인 자연수입니다.</li>
        <li>곱할 수 있는 배열만 주어집니다</li>
    </ul>
    <h3 id="_2">입출력의 예</h3>
    <table class="result-table">
        <thead>
            <tr>
                <th>arr1</th>
                <th>arr2</th>
                <th>return</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>[[1,4],[3,2],[4,1]]</td>
                <td>[[3,3],[3,3]]</td>
                <td>[[15,15],[15,15],[15,15]]</td>
            </tr>
            <tr>
                <td>[[2,3,2],[4,2,4][3,1,4]]</td>
                <td>[[5,4,3],[2,4,1],[3,1,1]]</td>
                <td>[[22,22,11],[36,28,18],[29,20,14]]</td>
            </tr>
        </tbody>
    </table>
    <h3 id="_3">문제 분석하고 풀기</h3>
    <p>수학의 행렬 곱셈을 그대로 구현하면 됩니다. 두 배열의 최대 데이터 개수가 100개이므로 시간 복잡도는 신경 쓰지 않아도 됩니다. 또한 행렬 곱할 수 있는 배열만 주어지므로 예외 처리도 없습니다.</p>
<pre><code>
def solution(arr1, arr2):
  # ➊ 행렬 arr1과 arr2의 행과 열의 수
  r1, c1 = len(arr1), len(arr1[0])
  r2, c2 = len(arr2), len(arr2[0])

  #_ ➋ 결과를 저장할 2차원 리스트 초기화
  ret = [[0] * c2 for _ in range(r1)]

  #_ ➌ 첫 번째 행렬 arr1의 각 행과 두 번째 행렬 arr2의 각 열에 대해
  for i in range(r1):
    for j in range(c2):
      # ➍ 두 행렬의 데이터를 곱해 결과 리스트에 더해줌
      for k in range(c1):
        ret[i][j] += arr1[i][k] * arr2[k][j]
  return ret
</code></pre>
    <p>여기서는 문제를 나누는 연습을 해보기 좋습니다. 간단한 문제도 막상 한꺼번에 풀려고 하면 잘 안 풀리는 경우가 많습니다. 행렬 곱셈에서 가장 먼저 행렬 곱셈의 결괏값을 어떻게 저장할지 고려해야 합니다. 결괏값을 저장하려면 두 행렬을 곱했을 때 결과 행렬의 크기를 알아야 합니다. 이건 행렬 정의를 안다면 쉽게 해결할 수 있습니다.</p>
    <p>➊ 인수로 받은 arr1과 arr2의 행과 열 정보를 변수에 기록합니다. 이후 행렬 정의를 활용해서 결과 행렬을 저장할 수 있는 크기의 새 행렬을 만들고 모든 데이터를 0으로 초기화합니다.</p>
    <p>➋ 결과 행렬의 크기는 (r1 * c2)이므로 해당 크기의 리스트를 미리 만들어 0으로 초기화합니다. 즉, ret에는 행렬 곱 결과가 저장됩니다. for _ in range 구문이 생소할 수 있습니다. 보통 _ 대신 i와 같은 변수를 사용해 반복문 내에서 사용하는 것이 일반적입니다. 하지만 반복문 내에서 변수를 사용하지 않을 수도 있습니다. 그럴 때는 관례적으로 _를 사용합니다. 앞으로도 반복문 내에서 변수를 사용하지 않다면 _를 사용하겠습니다.</p>
    <p>➌ arr1과 arr2의 행렬을 곱하기 위한 반복문입니다. 행렬을 곱할 땐 첫 번째 행렬의 각 행과 두 번째 행렬의 각 열들을 매치해 연산합니다. 이를 위해 반복문에서 첫 번째 행렬의 행의 크기인 r1과 두 번째 행렬의 열의 크기인 c2를 사용했습니다. </p>
    <p>➍에서는 첫 번째 행렬의 i번째 행과 두 번째 행렬의 j번째 열을 곱합니다. 마지막으로 반복문에서 곱 연산을 수행하며 ret 배열에 데이터를 저장하면 행렬 곱이 완성됩니다.</p>
    <h3 id="_4">시간 복잡도 분석하기</h3>
    <p>N은 행 혹은 열의 길이입니다. 행과 열의 길이는 같습니다. arr1의 행과 열 수를 r1, c1라고 하고, arr2의 행과 열 수를 r2, c2라고 했을때 r1c1c2만큼 연산합니다. r1, c1, r2, c2 모두 N으로 볼 수 있으므로 최종 시간 복잡도는 O(N3)입니다.</p>
</div>