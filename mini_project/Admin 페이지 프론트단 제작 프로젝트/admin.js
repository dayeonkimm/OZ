
document.addEventListener('DOMContentLoaded', function() {
    const titleElement = document.getElementById('title');
    const updateDateElement = document.getElementById('updateDate');
    
    // 현재 날짜 구하기
    const currentDate = new Date();
    const year = currentDate.getFullYear();
    const month = String(currentDate.getMonth() + 1).padStart(2, '0');
    const day = String(currentDate.getDate()).padStart(2, '0');

    // 업데이트 날짜 문자열 생성
    const updateDateString = `${year}-${month}-${day}`;

    // 업데이트 날짜 표시
    updateDateElement.textContent = `(업데이트 날짜: ${updateDateString})`;
});
      
      
      // 크롤링한 데이터를 아래와 같은 형태의 객체 배열로 가정
      // 추후 데이터베이스에 있는 데이터를 쿼리문으로 불러 올 수 있게 쿼리르 작성해 볼 수 있음
      // 데이터 예시 (임의로 배열에 저장된 것으로 가정)
const data = [
          { category: "상의", gender: "남성", brand: 'Supreme', product: '슈프림 박스로고 후드티', price: '390,000' },
          { category: "하의", gender: "남성", brand: 'DIESEL', product: '디젤 트랙 팬츠', price: '188,000' },
          { category: "신발", gender: "여성", brand: 'Nike', product: '에어포스 1', price: '137,000' },
          { category: "패션잡화", gender: "공용", brand: 'Music&Goods', product: '빵빵이 키링', price: '29,000' },
          // ...
      ];

// 테이블에 데이터 추가하는 함수
function populateTable(data) {
    const tableBody = document.querySelector('#myTable tbody');
    tableBody.innerHTML = ''; // 기존 테이블 내용 비우기

    data.forEach(function(item) {
        const row = tableBody.insertRow(); // 새로운 행 삽입

        // 체크박스 셀 추가
        const checkboxCell = row.insertCell();
        checkboxCell.innerHTML = '<input type="checkbox">';

        // 카테고리 셀 추가
        const categoryCell = row.insertCell();
        categoryCell.textContent = item.category;

        // 성별 셀 추가
        const genderCell = row.insertCell();
        genderCell.textContent = item.gender;

        // 브랜드 셀 추가
        const brandCell = row.insertCell();
        brandCell.textContent = item.brand; 

        // 제품 셀 추가
        const productCell = row.insertCell();
        productCell.textContent = item.product;

        
       // 데이터 셀 추가
       for (const key in item) {
            if (item.hasOwnProperty(key) && key !== 'category' && key !== 'gender' && key !== 'brand' && key !== 'product') {
                const cell = row.insertCell();
                cell.textContent = item[key];
            }
        }
    });
}

// 페이지 로드 시 테이블 데이터 생성
populateTable(data);

// 체크된 행 삭제 함수
function deleteCheckedRows() {
    const tableBody = document.querySelector('#myTable tbody');
    const rows = tableBody.querySelectorAll('tr');

    rows.forEach(function(row) {
        const checkbox = row.querySelector('input[type="checkbox"]');
        if (checkbox.checked) {
            tableBody.removeChild(row);
        }
    });
}

// 전체 선택 체크박스 이벤트 핸들러
const selectAllCheckbox = document.getElementById('selectAllCheckbox');
selectAllCheckbox.addEventListener('change', function() {
    const checkboxes = document.querySelectorAll('#myTable tbody input[type="checkbox"]');
    checkboxes.forEach(function(checkbox) {
        checkbox.checked = selectAllCheckbox.checked;
    });
});




// 필터링 함수
function filterTable() {
    const selectedCategory = document.getElementById('categorySelect').value;
    const selectedGender = document.querySelector('input[name="gender"]:checked').value;
    const inputText = document.getElementById('productInput').value.toLowerCase(); // 대소문자 구분 없이 비교하기 위해 소문자로 변환
    const rows = document.querySelectorAll('#myTable tbody tr');

    rows.forEach(function(row) {
        const categoryCell = row.cells[1]; // 카테고리 셀
        const genderCell = row.cells[2]; // 성별 셀
        const productCell = row.cells[4]; // 제품 셀

        const categoryMatch = selectedCategory === '전체' || categoryCell.textContent === selectedCategory;
        const genderMatch = selectedGender === '전체' || genderCell.textContent === selectedGender;
        const productMatch = inputText === '' || productCell.textContent.toLowerCase().includes(inputText);

        if (categoryMatch && genderMatch && productMatch) {
            row.style.display = ''; // 선택한 카테고리와 성별이 일치하고 제품이 포함된 경우 보이기
        } else {
            row.style.display = 'none'; // 그 외의 경우 숨기기
        }


        
    });
}

// 조회 버튼 클릭 시 필터링 함수 호출
document.getElementById('searchButton').addEventListener('click', filterTable);

// 카테고리 선택 변경 시 필터링 함수 호출
document.getElementById('categorySelect').addEventListener('change', filterTable);

// 성별 라디오 버튼 변경 시 필터링 함수 호출
document.querySelectorAll('input[name="gender"]').forEach(function(radio) {
    radio.addEventListener('change', filterTable);
}); 

document.getElementById('searchButton').addEventListener('click', function(event) {
    // 입력 필드의 값을 가져오기
    const inputValue = document.getElementById('productInput').value;
});



