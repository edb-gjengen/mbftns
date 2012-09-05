$(function() {
    $(".days").each( function(i, value) {
        $(value).click( function(event) {
            event.preventDefault();
            $(this).siblings().removeClass('active');
            $(this).addClass('active');
            $("#id_duration").val($(this).attr('data-days'));
        });
    });
    $("#id_duration").bind('change keyup', function(event) {
        $(".days").removeClass('active');
    });

    $("#id_duration").tooltip(
        {
            title: 'Antall dager. Brukeren kan ha varighet i maksimalt 120 dager (4 måneder).',
            placement: 'right'
        });
});
