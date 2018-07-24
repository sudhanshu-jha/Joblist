$(function () {

  /* Functions */

  var loadForm = function () {
    var btn = $(this);
    $.ajax({
      url: btn.attr("data-url"),
      type: 'get',
      dataType: 'json',
      beforeSend: function () {
        $("#modal-job .modal-content").html("");
        $("#modal-job").modal("show");
      },
      success: function (data) {
        $("#modal-job .modal-content").html(data.html_form);
      }
    });
  };

  var saveForm = function () {
    var form = $(this);
    $.ajax({
      url: form.attr("action"),
      data: form.serialize(),
      type: form.attr("method"),
      dataType: 'json',
      success: function (data) {
        if (data.form_is_valid) {
          $("#job-table tbody").html(data.html_job_list);
          $("#modal-job").modal("hide");
        }
        else {
          $("#modal-job .modal-content").html(data.html_form);
        }
      }
    });
    return false;
  };


  /* Binding */

  // Create job
  $(".js-create-job").click(loadForm);
  $("#modal-job").on("submit", ".js-job-create-form", saveForm);

  // Update job
  $("#job-table").on("click", ".js-update-job", loadForm);
  $("#modal-job").on("submit", ".js-job-update-form", saveForm);

  // Delete job
  $("#job-table").on("click", ".js-delete-job", loadForm);
  $("#modal-job").on("submit", ".js-job-delete-form", saveForm);

});
