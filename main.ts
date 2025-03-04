function suma(a: number, b: number): number {
    return a + b;
  }
  console.log(suma(5, 3)); // ✅ 8
  console.log(suma("5", 3)); // ❌ Error en tiempo de compilación
  