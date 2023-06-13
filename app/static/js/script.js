$(function() {

    $("#fasta_file").bind('change',function() {
        var fileSize = this.files[0];
        var sizeInKb = fileSize.size/1024;
        if (sizeInKb > 50) {
            $(this).addClass("is-invalid")
            this.value = "";
        }
        else {
            $(this).removeClass("is-invalid")
        }
    });

    $("form").on("submit",function(e) {
        if (($("#fasta_file").get(0).files.length == 0)) {
            if ($("#fasta_text").val() == "") {
                e.preventDefault();
            }
            const regex = /\s*>\S+(?: \S+)*\s+[ACGTacgt]+(?:\s+[ACGTacgt]+)*/;
            const seq = $("#fasta_text").val();
            if (!seq.match(regex)) {
                $("#fasta_text").addClass("is-invalid")
                e.preventDefault();
            } 
            else {
                $("#fasta_text").removeClass("is-invalid")
            }
        }

        if(grecaptcha.getResponse() == "") {
            e.preventDefault();
            $("#recaptcha-warning").show();
        } 
    })


    
    var fasta_example_1 = $.ajax({
        url: '/static/text/example1.txt',
        dataType: 'txt',
        async: false
    }
    ).responseText



    $('#example-btn').click(function() {
        $('#fasta_text').val(fasta_example_1);
        $('#fasta_text').change();
    });


    $(".fix-text").each(function () {
         $(this).text($(this).text().replace(/[^a-zA-Z1-9 .]/g,' '))
    });

    $(".date").each(function() {
        date_time = new Date($(this).text() + " UTC")
        $(this).text(date_time.toString())
    })

})