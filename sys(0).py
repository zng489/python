import time
import sys
class Task:
    def __init__(self, name, func, retries=0, timeout=None, sleep_time=0):
        self.name = name
        self.func = func
        self.dependencies = []  # nomes das tarefas upstream
        self.retries = retries
        self.timeout = timeout  # segundos
        self.sleep_time = sleep_time  # segundos

    def set_upstream(self, task):
        if task.name not in self.dependencies:
            self.dependencies.append(task.name)

    def __rshift__(self, other):
        """Operador para definir dependência: task1 >> task2"""
        other.set_upstream(self)
        return other

    def run(self):
        print(f"\n[>>>] Executando tarefa: {self.name}")
        start_time = time.time()

        for attempt in range(self.retries + 1):
            try:
                print(f"[...] Tentativa {attempt + 1} da tarefa '{self.name}'")

                if self.sleep_time > 0:
                    print(f"[...] Aguardando {self.sleep_time}s antes de executar '{self.name}'...")
                    time.sleep(self.sleep_time)

                print(f"[✓] Iniciando execução de '{self.name}'")
                result = self.func()

                elapsed = time.time() - start_time
                if self.timeout and elapsed > self.timeout:
                    raise TimeoutError(f"Tarefa '{self.name}' excedeu o tempo limite de {self.timeout}s")

                print(f"[✓] Tarefa '{self.name}' concluída com sucesso.")
                print(f"[O] Tarefa '{self.name}' levou {elapsed:.2f} segundos.")
                return result, elapsed  # Retorna também o tempo

            except Exception as e:
                print(f"[X] Erro ao executar a tarefa '{self.name}': {e}")
                if attempt < self.retries:
                    print(f"[...] Repetindo a tarefa '{self.name}'...\n")
                else:
                    print(f"[X] Tarefa '{self.name}' falhou após {self.retries + 1} tentativas.")
                    raise

        return None, 0


class Pipeline:
    def __init__(self, tasks):
        self.tasks = {task.name: task for task in tasks}

    def _execute_task(self, task, executed, task_times):
        for dep_name in task.dependencies:
            if dep_name not in executed:
                self._execute_task(self.tasks[dep_name], executed, task_times)

        result, elapsed = task.run()
        executed.add(task.name)

        # Salvar tempo da tarefa
        task_times[task.name] = elapsed

    def run(self):
        """Executa todas as tarefas em ordem de dependência"""
        executed = set()
        task_times = {}  # armazena tempo de cada tarefa
        print("[Pipeline] Iniciando pipeline sequencial...\n")

        pipeline_start = time.time()

        for task in self.tasks.values():
            if not task.dependencies:
                self._execute_task(task, executed, task_times)

        pipeline_end = time.time()
        total_time = pipeline_end - pipeline_start
        task_total_time = sum(task_times.values())

        print("\n[O] Tempos de Execução das Tarefas:")
        for name, t in task_times.items():
            print(f"- {name}: {t:.2f} segundos")

        print(f"\n[...] Tempo total do pipeline: {total_time:.2f} segundos")
        print(f"[...] dos tempos das tarefas: {task_total_time:.2f} segundos")
        print(f"[...] Sobrecarga (espera/repetição): {(total_time - task_total_time):.2f} segundos")

        print(f"\n[Pipeline] Execução concluída.")
        sys.exit(0)