function update_list_client(page=1, on_delete=false){
    var number_page = page;
    var count_itens = parseInt($('#id_page_itens').val());
    let url = ''
    query =  $("#id_query").val();
    const queryString = window.location.search;
    const urlParams = new URLSearchParams(queryString);

    console.log("page: ", number_page);
    console.log("itens page: ", $('#id_page_itens').val());

    if (urlParams.has('page')){
        number_page = urlParams.get('page')
    }
    if (count_itens==1 && number_page>1 && on_delete==true){
        number_page = number_page - 1;
        console.log("page: ", number_page);
    }
    if (query!==''){
        url = '/list_client/?query='+query+'&page='+number_page
        console.log("exist query: ", query);
    } else {
        url = '/list_client/?page='+number_page
    }

    $.ajax({
        type: 'GET',
        url: url,
        data: {},
        success: function(data){
                $("#list_clients").html(data);
            }
    });
}


function view_delete_client(id_client, name_client){
    let link_delete = id_client;
    console.log(link_delete);

    $.ajax({
        type: 'GET',
        url: '/delete/'+id_client+'/',
        data: {},
        success: function(data){
            $('#title_modal').empty();
            $('#title_modal').append('Confirmação!');
            $('.modal-body').empty();
            $('.modal-body').html(data);
            $('#button_action').removeAttr("onclick");
            $('#button_action').empty();
            $('#button_action').append("Deletar Cliente");

            $("#button_action").removeClass().addClass('btn btn-danger')
            $('#button_action').attr('onclick','delete_client('+ link_delete+')').unbind('click');
        }
    });
}



function view_client(id_client){
    $.ajax({
        type: 'GET',
        url: '/view_client/'+id_client+'/',
        data: {},
        success: function(data){
            $('#title_modal').empty();
            $('#title_modal').append('Dados do Cliente');
            $('.modal-body').empty();
            $('.modal-body').html(data);
            $('#button_action').removeAttr("onclick");
            $('#button_action').empty();
            $('#button_action').append("Editar Cliente");
            $("#button_action").removeClass().addClass('btn btn-warning text-white d-none')
            $('#button_action').attr('onclick',"location.href='/clientes/update/"+id_client+"/'").unbind('click');
        }
    });
}


function view_update_client(id_client, name_client){
    $.ajax({
        type: 'GET',
        url: '/update/'+id_client+'/',
        data: {},
        success: function(data){
            $('#title_modal').empty();
            $('#title_modal').append('Editar Cliente - '+name_client);
            $('.modal-body').empty();
            $('.modal-body').html(data);
            $('#button_action').removeAttr("onclick");
            $('#button_action').empty();
            $('#button_action').append("Editar");
            $("#button_action").removeClass().addClass('btn btn-warning')
            $("button_action").css("background-color", "#fd7700");
            $('#button_action').attr('onclick','update_client('+ id_client+')').unbind('click');
        }
    });
}

function update_client(id_client){
    var number_page = parseInt($('#id_page_index').val());
    var token = $('input[name="csrfmiddlewaretoken"]');
    $.ajax({
        method: "POST",
        url: '/update/'+id_client+'/',
        data: $('#client_form_'+id_client).serialize(),

        success: function (data) {
            if (data.updated) {
                console.log("atualizado com sucesso!");
                update_list_client(number_page);
                $('#modal_client').modal('hide');
            } else {
                console.log("error ao atualizar!");
                $('.modal-body').empty();
                $('.modal-body').html(data);

            }
        }
     });
}


function delete_client(id){
    var number_page = parseInt($('#id_page_index').val());
    var token = $('input[name="csrfmiddlewaretoken"]');
    $.ajax({
        method: "POST",
        url: '/delete/'+id+'/',
        data: $('#client_form_'+id).serialize(),

        success: function (data) {
            if (data.deleted) {
                update_list_client(number_page, true);
                $('#modal_client').modal('hide');
            } else {
                console.log("error ao cadastrar!");
                $('.modal-body').empty();
                $('.modal-body').html(data);

            }
        }
     });
}

function view_create_client(){
    $.ajax({
        type: 'GET',
        url: '/create/',
        data: {},
        success: function(data){
            $('#title_modal').empty();
            $('#title_modal').append('Adicionar Novo Cliente');
            $('.modal-body').empty();
            $('.modal-body').html(data);
            $('#button_action').removeAttr("onclick");
            $('#button_action').empty();
            $('#button_action').append("Adicionar");
            $("#button_action").removeClass().addClass('btn btn-primary text-white')
            $('#button_action').attr('onclick','create_client()').unbind('click');
        }
    });
}

function create_client(){
    var number_page = parseInt($('#id_page_index').val());
    $.ajax({
        method: "POST",
        url: '/create/',
        data: $('#client_form_0').serialize(),

        success: function (data) {

            if (data.created) {
                console.log("atualizado com sucesso!");
                update_list_client(number_page);
                $('#modal_client').modal('hide');
            } else {
                console.log("error ao cadastrar!");
                $('.modal-body').empty();
                $('.modal-body').html(data);

            }
        }
     });
}