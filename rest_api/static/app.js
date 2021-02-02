function show_id(event)
{

    var id = this.dataset.id;
    var address = '/get_car_by_type?type_id=' + id;
    fetch(address)
        .then(response => response.text())
        .then(data => document.getElementById("cars").innerHTML = data);

}



$( document ).ready(function() {
    var li_buttons = $('.type');
    li_buttons.click(show_id);
});