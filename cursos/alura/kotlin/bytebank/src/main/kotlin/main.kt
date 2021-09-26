fun main(){
    println("Seja bem vindo(a) ao ByteBank")

    val conta1 = Conta("Iago Reis", 1)
    conta1.depositar(100.0)

    val conta2 = Conta(titular = "Mundo Dev", numero = 2)
    conta2.depositar(99.99)

    println(conta1)
    println(conta2)
    println()

    var valor = 100.0

    conta2.depositar(500.00)
    println(conta2)
    println()

    valor = 500.0
    conta2.sacar(valor)
    println(conta2)
    println()

    valor = 199.99
    conta2.sacar(valor)
    println(conta2)
    println()

    valor = 50.0
    conta1.transferir(valor, conta2)
    println(conta1)
    println(conta2)
    println()

    valor = 500.0
    conta1.transferir(valor, conta2)
    println(conta1)
    println(conta2)
    println()
}

class Conta(val titular: String, val numero: Int) {

    var saldo: Double = 0.0
        private set

    fun depositar(valor: Double) {
        println("Depositando $valor na conta ${this.titular}")
        if (valor > 0.0) {
            this.saldo += valor
        }
    }

    fun sacar(valor: Double): Double {
        println("Sacando $valor da conta ${this.titular}")
        if (this.possuiSaldoSuficiente(valor)) {
            this.saldo -= valor
            println("Saque realizado com sucesso")
            return valor
        }
        println("Saque não realizado")
        return 0.0
    }

    fun transferir(valor: Double, contaDestino: Conta): Boolean {
        println("Transferindo $valor da conta ${this.titular} para a conta ${contaDestino.titular}")
        if (this.possuiSaldoSuficiente(valor)) {
            this.sacar(valor)
            contaDestino.depositar(valor)
            println("Transferência realizada com sucesso")
            return true
        }
        println("Transferência não realizada")
        return false
    }

    fun possuiSaldoSuficiente(valor: Double): Boolean {
        return this.saldo >= valor
    }

    override fun toString(): String {
        return "Conta [titular: $titular, numero: $numero, saldo: $saldo]"
    }

}