# bAbi-tasks-transformer-train
Fine tune and evaluate transformer model on facebook's bAbi tasks.
> [Towards AI-Complete Question Answering: A Set of Prerequisite Toy Tasks](https://arxiv.org/abs/1502.05698)

* Train: [trainer.py](trainer.py)

* Evaluation: [eval.py](eval.py)


## Tasks
|task_no|task_name|
|----|------------|
|qa1 |single-supporting-fact|
|qa2 |two-supporting-facts|
|qa3 |three-supporting-facts|
|qa4 |two-arg-relations|
|qa5 |three-arg-relations|
|qa6 |yes-no-questions|
|qa7 |counting|
|qa8 |lists-sets|
|qa9 |simple-negation|
|qa10| indefinite-knowledge|
|qa11| basic-coreference|
|qa12| conjunction|
|qa13| compound-coreference|
|qa14| time-reasoning|
|qa15| basic-deduction|
|qa16| basic-induction|
|qa17| positional-reasoning|
|qa18| size-reasoning|
|qa19| path-finding|
|qa20| agents-motivations|


## Acknowledgements:

Based on original: https://github.com/p208p2002/bAbi-tasks-with-transformer-model

## Description

Разделив обучение на **два вида сэмплов**, ты чётко учишь:

* одна подзадача = **трекер слотов памяти (текущих состояний)**,

* вторая подзадача = **генератор ответа**.

### В итоге будет пайплайн:

* 1. User turn + context → Slot-states (обновлённый). Тут System-response можно вообще не добавлять.

* 2. Slot-states + User turn → System-response.
