//Exercício E2- POOII

#include <iostream>
#include <typeinfo>
#include <cxxabi.h>

// Função auxiliar para obter o nome de tipo demangled
std::string demangle(const char* name) {
    int status;
    char* demangled_name = abi::__cxa_demangle(name, nullptr, nullptr, &status);
    std::string result(demangled_name);
    free(demangled_name);
    return result;
}

// Classe exemplo
class MinhaClasse {
public:
    int x;

    MinhaClasse(int x) : x(x) {}

    void meuMetodo() {
        std::cout << "Executando o método" << std::endl;
    }
};

int main() {
    // Obtendo informações sobre a classe
    const std::type_info& classe = typeid(MinhaClasse);
    std::string nomeDaClasse = demangle(classe.name());
    std::cout << "Nome da classe: " << nomeDaClasse << std::endl;

    // Obtendo informações sobre os métodos da classe
    // (A inspeção detalhada de métodos em C++ é mais complexa e depende do compilador)
    std::cout << "Métodos da classe:" << std::endl;
    std::cout << " - meuMetodo" << std::endl;

    // Executando um método da classe
    MinhaClasse instancia(5);
    instancia.meuMetodo();

    return 0;
}

//Fonte: C++ Reference: typeid - https://en.cppreference.com/w/cpp/language/typeid