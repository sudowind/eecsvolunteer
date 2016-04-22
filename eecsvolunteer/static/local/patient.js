/**
 * Created by Wind on 2016/4/19.
 */
function add_case() {
    var owner = $('#owner').val();
    var contact = $('#contact').val();
    var model = $('#computer_model').val();
    var problem = $('#problem').val();
    if (owner == '' || model == '' || problem == '') {
        tips('请填写缺失项', 'info');
        return;
    }
    var wait_count;
    var id;
    var csrftoken = getCookie('csrftoken');
    $.ajax({
        url: 'add_case/',
        method: 'post',
        dataType: 'json',
        data: {
            csrfmiddlewaretoken: csrftoken,
            owner: owner,
            contact: contact,
            model: model,
            problem: problem
        },
        async: false,
        success: function(data) {
            if (data['code'] == 1) {
                tips('添加成功', 'success');
                wait_count = data['wait_count'];
                id = data['id']
                //$('#info_message').html(
                //    '<span style="color: green">流水号:' + id + ',还需等待' + wait_count.toString() + '人</span><br />'
                //);
                $('#owner_info').html('<strong>机主:</strong>' + owner);
                $('#contact_info').html('<strong>联系方式:</strong>' + contact);
                $('#model_info').html('<strong>机型:</strong>' + model);
                $('#problem_info').html('<strong>问题描述:</strong>' + problem);
                $('#wait_info').html('<strong>等待人数:</strong>' + wait_count.toString());
                $('#num_info').html('<strong>流水号:</strong>' + id.toString());
                $('#create_case').hide();
            }
            else {
                var msg = data['msg'] || '添加失败';
                tips(msg, 'error');
            }
        },
        error: function() {
            tips('连接超时', 'error');
        }
    });
}