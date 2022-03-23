$(document).ready(function() {
    $("#id_instance_name").change(function() {
        var django_host= '127.0.0.1:8000';
        var instance_nm =$("#id_instance_name option:selected").text();
        var url_svr="http://"+django_host+"/infrastructure/ServersALL_JSON/"+instance_nm
  
        var server_name_dd = $("#id_Server");
        $('#id_Server >option').remove();
        $.ajax({
            url: url_svr,
            type: "GET",
            dataType: "json",
            cache: false,
            contentType:"application/json; charset=utf-8",
  
            success: function(data) {
              $.each( data, function(index,value) {
                server_name_dd.append($("<option />").val(value.id).text(value.name));
              });
              $('#id_Server').multiselect('rebuild');
            },
            error: function(xhr, textStatus) {
              console.log("error..");
            }
        }); 
     });
  });
