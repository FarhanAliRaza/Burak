if (document.readyState == "loading") {
  document.addEventListener("DOMContentLoaded", () => {
    ready();
  });
} else {
  ready();
}

function ready() {
  let addToCartButtons = $("a#shop-btn");
  for (let i = 0; i < addToCartButtons.length; i++) {
    let button = addToCartButtons[i];
    button.addEventListener("click", () => {
      let id = button.dataset.id;
      let title = button.dataset.title;
      let price = button.dataset.price;
      console.log(title);
      console.log(price);
      addItemToCart(title, price, id);
    });
  }
}

function addItemToCart(title, price, id) {
  let cartRow = document.getElementById("items");
  let cartRowContents = `
        <div id="item">
          <div id="all" class="row">
          <div class="col-3">
              <div>
                  <h2>${title}</h2>
              </div>
          </div>
          <div class="col-3">
              <div>
                  <div class="stepper stepper-lg ">
                    <a href="#" id="m" class="stepper-button btn-primary " ><h1 style="color : white ;">-</h1></a>
                    <input type="text" min="1" id="q" class="form-control" value="1" disabled />
                    <a href="#" id="p" class="stepper-button btn-primary"><h2 style="color : white ;">+</h2></a>
                  </div>
              </div>
          </div>
          <div class="col-3">
              <div>
                  <h3 id="price" style="margin-left:10px; font-size: 30px;">${price}</h3>
              </div>
          </div>
          <div class="col-3">
              <div>
                  <button id="del" class="btn btn-outline-danger btn-sm" type = "submit">Delete</button>
              </div>
          </div>
        </div>
        </div>`;
  cartRow.innerHTML = cartRowContents;
  $("button#del").click(function (e) {
    $("div#item").detach();
    $("#actionSheetForm").modal("hide");
  });

  $("a#p").click(function (e) {
    let q = parseInt($("input#q").val());
    console.log(q + 1);
    q = q + 1;
    $("input#q").val(q);
    let p = parseInt(price);
    let newPrice = q * p;
    $("h3#price").html(newPrice);
  });
  $("a#m").click(function (e) {
    let q = parseInt($("input#q").val());
    if (q == 1) {
      v = 1;
      $("input#q").val(v);
    } else {
      v = q - 1;
      $("input#q").val(v);
    }

    let p = parseInt(price);
    let newPrice = v * p;
    $("h3#price").html(newPrice);
  });

  $("button#continue").one("click", con);
  $("button#check").one("click", check);
  function con() {
    q = parseInt($("input#q").val());
    
    $.ajax({
      type: "GET",
      url: "/ajax/add",
      data: { id, q },
      success: function (data) {
        $("#actionSheetForm").modal("hide");
        $("div#item").detach();
        location.reload();
        console.log("success");
      },
    });
  }
  function check() {
    q = parseInt($("input#q").val());
    $.ajax({
      type: "GET",
      url: "/ajax/add",
      data: { id, q },
      success: function (data) {
        console.log("success");
        window.location.href = "/ajax/cart";
      },
    });
  }
}

//cart Page
function cart() {
  $("button#delete").one("click", function (e) {
    let button = $("button#delete");
    let id = button.data("id");
    $(`div#${id}`).detach();
    $.ajax({
      type: "GET",
      url: "/ajax/delete",
      data: { id },
      success: function (data) {
        console.log("success");
        location.reload();
      },
    });
  });

 
}
