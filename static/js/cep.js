$("#cep").focusout(function(){

			$.ajax({

				url: 'https://viacep.com.br/ws/'+$(this).val()+'/json/',
				dataType: 'json',
				success: function(resposta){

					$("#endereco").val(resposta.logradouro);
					$("#bairro").val(resposta.bairro);
					$("#cidade").val(resposta.localidade);
					$("#pais").val('Brasil');
					$("#estado").val(resposta.uf);

				}
			});
		});