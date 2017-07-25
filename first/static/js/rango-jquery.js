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
                $.post('/rango/like_category/', {category_id: catid}, function (data) {
                    // console.log(data)
                    $('#like_count').html(data);
                    $('#likes').hide();
                });



        });
        $("#suggestion").keyup(function () {
            var query;
            query = $(this).val();
            $.get('/rango/suggest_category', {suggestion: query}, function (data) {
                // console.log(data)
                $('#cats').html(data)

            })

        })

        $('.rango-add').click(function () {
            var catid = $(this).attr('data-catid');
            var url = $(this).attr('data-url');
            var title = $(this).attr('data-title');
            var  me =$(this);
            $.post('/rango/auto_add_page/', {category_id:catid, url:url, title:title},function (data) {
                console.log(data)
                $('#pages').html(data);
                me.hide();
            })

        })

        });
