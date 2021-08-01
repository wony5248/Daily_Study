
// IIFE

(async function () {
    const menus = [{
            id: 1,
            menu: "치킨",
            price: 2000
        },
        {
            id: 2,
            menu: "피자",
            price: 4000
        },
        {
            id: 3,
            menu: "곱창",
            price: 6000
        },
        {
            id: 4,
            menu: "초밥",
            price: 8000
        },
    ];

    function sleep(time) {
        return new Promise(function (resolve, reject) {
            setTimeout(() => {
                resolve()
            }, 1000)
        });
    }

    const trTag = (data) => {

        return `
        <tr>
            <th scope="row">${data.id}</th>
            <td>${data.menu}</td>
            <td>${data.price}</td>
        </tr>`
    }

    const makingTable = () => {
        
        const trTags = menus.reduce((acc, cur) => {
            acc += trTag(cur);
            return acc;
        },"")

        return `
        <table class="table">
            <thead>
              <tr>
                <th scope="col">#</th>
                <th scope="col">메뉴</th>
                <th scope="col">가격</th>
              </tr>
            </thead>
            <tbody>
                ${trTags}
            </tbody>
          </table>
          `
    }

    await sleep(1000);
    document.querySelector("body").style.backgroundColor = "blue"
    await sleep(1000);
    document.querySelector("body").style.backgroundColor = "white"
    await sleep(2000);
    document.querySelector(".container").innerHTML = makingTable()
})();