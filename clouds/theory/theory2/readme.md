Выполнила: Данилова Анастасия Алексеевна

Вариант: 6

# Рубежные работы по Облачным технологиям

### Работа 2.

## Вопрос:

_Допустим, у вас развернута большая инфраструктура: сотни виртуальных машин, десятки разных
сервисов. Как будете мониторить состояние инфраструктуры? Интересуют логи, отказы, нагрузка и
тд. Приведите пример для любого из провайдеров_

## Ответ:

Для мониторинга инфраструктуры с большим количеством виртуалок и различных сервисов можно воспользоваться облачным сервисом Amazon Web Services.

### Amazon CloudWatch

Для отслеживания логов, отказов и нагрузки хорошим вариантом будет **Amazon CloudWatch**. Это основной сервис для мониторинга ресурсов и приложений AWS. Он собирает и хранит метрики и файлы логов, устанавливает оповещения и даёт информацию об использовании ресурсов, производительности приложений и поведении системы. ([источник](https://dzone.com/articles/logging-and-monitoring-in-aws))

Он собирает и анализирует различные метрики(CPU, память, сеть), обрабатывает логи с помощью CloudWatch Logs и позволяет настраивать оповещения, например отправлять уведомления в случае превышения нагрузки.

### AWS CloudTrail.

Для отслеживания всех действий в аккаунте AWS и использования API можно использвовать **AWS CloudTrail.**

**AWS CloudTrail** - это сервис, который помогает отслеживать активность в среде AWS.
Он мониторит все вызовы с API и операции с ресурсами, а также действия AWS для выявления подозрительных действий.

### Amazon OpenSearch Service и Kibana

Amazon OpenSearch Service и Kibana можно объединить для более глубокого мониторинга данных и визуализировать их для более удобного взаимодействия с данными

OpenSearch интегрируется с сервисами AWS, такими как **CloudWatch Logs** и Lambda, для агрегации логов, а с Kibana - для визуализации данных.

### AWS Systems Manager

AWS Systems Manager - это сервис, с помощью которого можно управлять инфраструктурой.

Учитывая, что по ТЗ в проекте есть очень много виртуальнвх машин, то их надо как-то мониторить в том числе. AWS Systems Manager как раз автоматически обновляет систему и мониторит состояние виртуальных машин (EC2).

Он упрощает задачи, связанные с управлением системы и приложений, патчами, конфигурацией и автоматизацией, позволяя поддерживать здоровье и соответствие среды.

Симбиоз этих сервисов покроет большинство потребностей мониторнга и обеспечит гибкую, стабильную, безопасную и прозрачную работу инфраструктуры.
