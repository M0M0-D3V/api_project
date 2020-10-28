$(document).ready(function () {
    var html_str = "";
    for (var i = 1; i <= 150; i++) {
        html_str += `<img id="${i}" src="https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/${i}.png">`
    }
    $('.pokemon').append(html_str)

    $('img').hover(function () {
        var targetId = $(this).attr('id');
        console.log(targetId)

        var url = `https://pokeapi.co/api/v2/pokemon/${targetId}`
        console.log(url);

        $.get(url, function (res) {
            var infoStr = "";
            infoStr += "<ul>";
            infoStr += "<li><h2>" + res.name + "</h2></li>";
            infoStr += "<li><h3><img src=" + res.sprites.front_default + "></h3></li>";
            infoStr += "<li><h3>Number Types: " + res.types.length + "</h3></li>";
            infoStr += "<ul>";
            for (var i = 0; i < res['types'].length; i++) {
                console.log(res['types'][i]['type'])
                infoStr += "<li><p>" + res['types'][i]['type']['name'] + "</p></li>";
            }
            infoStr += "</ul>";
            infoStr += "<li><h3>Height: " + res.height + "</h3></li>";
            infoStr += "<li><h3>Weight: " + res.weight + "</h3></li>"
            $(".dex").html(infoStr);
        }, "json");
        // })
    })
})