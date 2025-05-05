
from qiskit import QuantumCircuit, transpile
import pygame
from qiskit.visualization import plot_histogram
from qiskit_aer import Aer



def grover_algorithm(target):
    # ایجاد مدار کوانتومی
    n_qubits = 3
    qc = QuantumCircuit(n_qubits, n_qubits)

    # پیاده‌سازی ساده‌شده‌ی الگوریتم گروور
    qc.h(range(n_qubits))
    # اوراکل (مثلاً عدد ۵ را هدف بگیریم)
    if target == 5:
        qc.z(0)  # یک اوراکل ساده
    qc.h(range(n_qubits))
    qc.measure(range(n_qubits), range(n_qubits))

    # اجرا روی شبیه‌ساز
    simulator = Aer.get_backend('qasm_simulator')
    result = simulator.result()
    counts = result.get_counts(qc)
    return counts


print(grover_algorithm(5))


pygame.init()
screen = pygame.display.set_mode((800, 600))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # فراخوانی الگوریتم کوانتومی
                result = grover_algorithm(5)
                print("نتیجه کوانتومی:", result)

    pygame.display.flip()

IBMQ.save_account('API_KEY')  # کلید API از حساب IBM
provider = IBMQ.load_account()
backend = provider.get_backend('ibmq_lima')
result = execute(qc, backend, shots=1024).result()