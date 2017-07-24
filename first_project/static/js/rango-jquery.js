$(document).ready(function() {
        $("#about-btn").click( function (event) {
                alert("You clicked the button using JQuery!");

        }

        )
        $("p").hover( function () {
                $(this).css('color','red');

        },function () {
                $(this).css('color','blue');

            }
        )
        $("#about-btn").addClass('btn btn-primary')

        // JQuery code to be added in here.
        $("#about-btn").click( function (event){
            msgstr=$("#msg").html()
            msgstr = msgstr +'o'
            $('#msg').html(msgstr)
        });

        $("#likes").click(function () {
                var catid;
                catid = $(this).attr("data-catid");
                $.get('rango/like_category/',{category_id: catid}, function (data) {
                    $('like-count').html(data)
                    $('#likes').hide();
                })



        });

        });
