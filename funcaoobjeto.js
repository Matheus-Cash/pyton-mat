const cliente = {
    nome: 'João',
    idade: 30,
    email: 'joaosilva5@gmail.com',
    telefone: '123-456-7867',
    saldo: 100.50,

    efetuarpagamento: function (valor) {
        if (valor > this.saldo) {
            console.log('saldo insuficiente');
        } else {
            this.saldo -= valor;
            console.log(`novo saldo ${this.saldo}`);
        }
    }
};

cliente.efetuarpagamento(300);