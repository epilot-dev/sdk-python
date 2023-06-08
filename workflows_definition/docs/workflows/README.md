# workflows

### Available Operations

* [create_definition](#create_definition) - createDefinition
* [delete_definition](#delete_definition) - deleteDefinition
* [get_definition](#get_definition) - getDefinition
* [get_definitions](#get_definitions) - getDefinitions
* [get_max_allowed_limit](#get_max_allowed_limit) - getMaxAllowedLimit
* [get_workflow_closing_reasons](#get_workflow_closing_reasons) - getWorkflowClosingReasons
* [set_workflow_closing_reasons](#set_workflow_closing_reasons) - setWorkflowClosingReasons
* [update_definition](#update_definition) - updateDefinition

## create_definition

Create a Workflow Definition.

### Example Usage

```python
import sdk
from sdk.models import shared

s = sdk.SDK(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = shared.WorkflowDefinition(
    assigned_to=[
        'maiores',
        'molestiae',
        'quod',
        'quod',
    ],
    closing_reasons=[
        shared.ClosingReasonID(
            id='x739cew',
        ),
        shared.ClosingReasonID(
            id='x739cew',
        ),
    ],
    creation_time='2021-04-27T12:01:13.000Z',
    description='totam',
    due_date='2021-04-27T12:00:00.000Z',
    dynamic_due_date=shared.DynamicDueDate(
        action_type_condition=shared.DynamicDueDateActionTypeCondition.STEP_CLOSED,
        number_of_units=6788.8,
        step_id='dicta',
        time_period=shared.DynamicDueDateTimePeriod.MONTHS,
    ),
    enable_ecp_workflow=False,
    flow=[
        shared.Step(
            assigned_to=[
                'deleniti',
            ],
            automation_config=shared.StepAutomationConfig(
                flow_id='hic',
            ),
            due_date='2021-04-27T12:00:00.000Z',
            dynamic_due_date=shared.DynamicDueDate(
                action_type_condition=shared.DynamicDueDateActionTypeCondition.STEP_CLOSED,
                number_of_units=5218.48,
                step_id='beatae',
                time_period=shared.DynamicDueDateTimePeriod.WEEKS,
            ),
            ecp=shared.ECPDetails(
                label='molestiae',
            ),
            execution_type=shared.StepType.MANUAL,
            id='2cb73920-5929-4396-bea7-596eb10faaa2',
            name='Stacy Champlin',
            order=6078.31,
            requirements=[
                shared.StepRequirement(
                    condition=shared.StepRequirementCondition.CLOSED,
                    definition_id='minima',
                    type=shared.ItemType.SECTION,
                ),
                shared.StepRequirement(
                    condition=shared.StepRequirementCondition.CLOSED,
                    definition_id='accusantium',
                    type=shared.ItemType.STEP,
                ),
            ],
            type=shared.ItemType.SECTION,
            user_ids=[
                9589.5,
                1020.44,
                6527.9,
                2088.76,
            ],
        ),
        shared.Step(
            assigned_to=[
                'repellat',
            ],
            automation_config=shared.StepAutomationConfig(
                flow_id='mollitia',
            ),
            due_date='2021-04-27T12:00:00.000Z',
            dynamic_due_date=shared.DynamicDueDate(
                action_type_condition=shared.DynamicDueDateActionTypeCondition.STEP_CLOSED,
                number_of_units=2532.91,
                step_id='commodi',
                time_period=shared.DynamicDueDateTimePeriod.WEEKS,
            ),
            ecp=shared.ECPDetails(
                label='molestiae',
            ),
            execution_type=shared.StepType.MANUAL,
            id='9251aa52-c3f5-4ad0-99da-1ffe78f097b0',
            name='Bessie Grady II',
            order=2961.4,
            requirements=[
                shared.StepRequirement(
                    condition=shared.StepRequirementCondition.CLOSED,
                    definition_id='dicta',
                    type=shared.ItemType.SECTION,
                ),
                shared.StepRequirement(
                    condition=shared.StepRequirementCondition.CLOSED,
                    definition_id='enim',
                    type=shared.ItemType.SECTION,
                ),
            ],
            type=shared.ItemType.STEP,
            user_ids=[
                641.47,
                2168.22,
                6924.72,
                5651.89,
            ],
        ),
        shared.Step(
            assigned_to=[
                'modi',
                'praesentium',
                'rem',
                'voluptates',
            ],
            automation_config=shared.StepAutomationConfig(
                flow_id='quasi',
            ),
            due_date='2021-04-27T12:00:00.000Z',
            dynamic_due_date=shared.DynamicDueDate(
                action_type_condition=shared.DynamicDueDateActionTypeCondition.STEP_CLOSED,
                number_of_units=5759.47,
                step_id='veritatis',
                time_period=shared.DynamicDueDateTimePeriod.MONTHS,
            ),
            ecp=shared.ECPDetails(
                label='incidunt',
            ),
            execution_type=shared.StepType.MANUAL,
            id='0ad2abd4-4269-4802-9502-a94bb4f63c96',
            name='Terence Marquardt',
            order=8915.55,
            requirements=[
                shared.StepRequirement(
                    condition=shared.StepRequirementCondition.CLOSED,
                    definition_id='dolorum',
                    type=shared.ItemType.STEP,
                ),
                shared.StepRequirement(
                    condition=shared.StepRequirementCondition.CLOSED,
                    definition_id='in',
                    type=shared.ItemType.SECTION,
                ),
                shared.StepRequirement(
                    condition=shared.StepRequirementCondition.CLOSED,
                    definition_id='maiores',
                    type=shared.ItemType.SECTION,
                ),
                shared.StepRequirement(
                    condition=shared.StepRequirementCondition.CLOSED,
                    definition_id='dicta',
                    type=shared.ItemType.STEP,
                ),
            ],
            type=shared.ItemType.SECTION,
            user_ids=[
                4118.2,
                3965.06,
                6754.39,
                8811.04,
            ],
        ),
    ],
    id='395efb9b-a88f-43a6-a997-074ba4469b6e',
    last_update_time='2021-04-27T12:01:13.000Z',
    name='Ms. Julie Gusikowski',
    update_entity_attributes=[
        shared.UpdateEntityAttributes(
            source=shared.UpdateEntityAttributesSource.CURRENT_SECTION,
            target=shared.UpdateEntityAttributesTarget(
                entity_attribute='my_status',
                entity_schema='opportunity',
            ),
        ),
        shared.UpdateEntityAttributes(
            source=shared.UpdateEntityAttributesSource.CURRENT_SECTION,
            target=shared.UpdateEntityAttributesTarget(
                entity_attribute='my_status',
                entity_schema='opportunity',
            ),
        ),
        shared.UpdateEntityAttributes(
            source=shared.UpdateEntityAttributesSource.WORKFLOW_STATUS,
            target=shared.UpdateEntityAttributesTarget(
                entity_attribute='my_status',
                entity_schema='opportunity',
            ),
        ),
    ],
    user_ids=[
        9689.62,
        6521.03,
        3209.97,
    ],
)

res = s.workflows.create_definition(req)

if res.workflow_definition is not None:
    # handle response
```

## delete_definition

Delete Workflow Definition.

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = operations.DeleteDefinitionRequest(
    definition_id='eum',
)

res = s.workflows.delete_definition(req)

if res.status_code == 200:
    # handle response
```

## get_definition

Get specific Definition by id from the Organization.

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = operations.GetDefinitionRequest(
    definition_id='dolor',
)

res = s.workflows.get_definition(req)

if res.workflow_definition is not None:
    # handle response
```

## get_definitions

Retrieve all Workflow Definitions from an Organization

### Example Usage

```python
import sdk


s = sdk.SDK(
    security=shared.Security(
        bearer_auth="",
    ),
)


res = s.workflows.get_definitions()

if res.workflow_definitions is not None:
    # handle response
```

## get_max_allowed_limit

Get limits and number of created executions for an Organization.

### Example Usage

```python
import sdk


s = sdk.SDK(
    security=shared.Security(
        bearer_auth="",
    ),
)


res = s.workflows.get_max_allowed_limit()

if res.max_allowed_limit is not None:
    # handle response
```

## get_workflow_closing_reasons

Returns all closing reasons defined for the workflow.

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = operations.GetWorkflowClosingReasonsRequest(
    definition_id='necessitatibus',
)

res = s.workflows.get_workflow_closing_reasons(req)

if res.closing_reasons_ids is not None:
    # handle response
```

## set_workflow_closing_reasons

Sets which closing reasons are defined for this workflow, based on the entire closing reasons catalog.

### Example Usage

```python
import sdk
from sdk.models import operations, shared

s = sdk.SDK(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = operations.SetWorkflowClosingReasonsRequest(
    closing_reasons_ids=shared.ClosingReasonsIds(
        reasons=[
            shared.ClosingReasonID(
                id='x739cew',
            ),
        ],
    ),
    definition_id='nemo',
)

res = s.workflows.set_workflow_closing_reasons(req)

if res.status_code == 200:
    # handle response
```

## update_definition

Update Workflow Definition.

### Example Usage

```python
import sdk
from sdk.models import operations, shared

s = sdk.SDK(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = operations.UpdateDefinitionRequest(
    workflow_definition=shared.WorkflowDefinition(
        assigned_to=[
            'iure',
        ],
        closing_reasons=[
            shared.ClosingReasonID(
                id='x739cew',
            ),
            shared.ClosingReasonID(
                id='x739cew',
            ),
            shared.ClosingReasonID(
                id='x739cew',
            ),
            shared.ClosingReasonID(
                id='x739cew',
            ),
        ],
        creation_time='2021-04-27T12:01:13.000Z',
        description='debitis',
        due_date='2021-04-27T12:00:00.000Z',
        dynamic_due_date=shared.DynamicDueDate(
            action_type_condition=shared.DynamicDueDateActionTypeCondition.WORKFLOW_STARTED,
            number_of_units=8061.94,
            step_id='deleniti',
            time_period=shared.DynamicDueDateTimePeriod.MONTHS,
        ),
        enable_ecp_workflow=False,
        flow=[
            shared.Section(
                id='1e5b7fd2-ed02-4892-9cdd-c692601fb576',
                name='Gary Streich',
                order=166.27,
                steps=[
                    shared.Step(
                        assigned_to=[
                            'aut',
                        ],
                        automation_config=shared.StepAutomationConfig(
                            flow_id='cumque',
                        ),
                        due_date='2021-04-27T12:00:00.000Z',
                        dynamic_due_date=shared.DynamicDueDate(
                            action_type_condition=shared.DynamicDueDateActionTypeCondition.WORKFLOW_STARTED,
                            number_of_units=9441.24,
                            step_id='libero',
                            time_period=shared.DynamicDueDateTimePeriod.MONTHS,
                        ),
                        ecp=shared.ECPDetails(
                            label='dolores',
                        ),
                        execution_type=shared.StepType.MANUAL,
                        id='87053202-c73d-45fe-9b90-c28909b3fe49',
                        name='Casey Stracke',
                        order=7301.22,
                        requirements=[
                            shared.StepRequirement(
                                condition=shared.StepRequirementCondition.CLOSED,
                                definition_id='quaerat',
                                type=shared.ItemType.SECTION,
                            ),
                            shared.StepRequirement(
                                condition=shared.StepRequirementCondition.CLOSED,
                                definition_id='aliquid',
                                type=shared.ItemType.STEP,
                            ),
                            shared.StepRequirement(
                                condition=shared.StepRequirementCondition.CLOSED,
                                definition_id='dolorem',
                                type=shared.ItemType.STEP,
                            ),
                            shared.StepRequirement(
                                condition=shared.StepRequirementCondition.CLOSED,
                                definition_id='qui',
                                type=shared.ItemType.STEP,
                            ),
                        ],
                        type=shared.ItemType.SECTION,
                        user_ids=[
                            7395.51,
                            4521.09,
                            4904.59,
                        ],
                    ),
                    shared.Step(
                        assigned_to=[
                            'amet',
                            'dolorum',
                            'numquam',
                            'veritatis',
                        ],
                        automation_config=shared.StepAutomationConfig(
                            flow_id='ipsa',
                        ),
                        due_date='2021-04-27T12:00:00.000Z',
                        dynamic_due_date=shared.DynamicDueDate(
                            action_type_condition=shared.DynamicDueDateActionTypeCondition.WORKFLOW_STARTED,
                            number_of_units=4344.17,
                            step_id='odio',
                            time_period=shared.DynamicDueDateTimePeriod.DAYS,
                        ),
                        ecp=shared.ECPDetails(
                            label='accusamus',
                        ),
                        execution_type=shared.StepType.AUTOMATION,
                        id='f69280d1-ba77-4a89-abf7-37ae4203ce5e',
                        name='Rosie McKenzie',
                        order=5197.11,
                        requirements=[
                            shared.StepRequirement(
                                condition=shared.StepRequirementCondition.CLOSED,
                                definition_id='alias',
                                type=shared.ItemType.SECTION,
                            ),
                            shared.StepRequirement(
                                condition=shared.StepRequirementCondition.CLOSED,
                                definition_id='quaerat',
                                type=shared.ItemType.STEP,
                            ),
                            shared.StepRequirement(
                                condition=shared.StepRequirementCondition.CLOSED,
                                definition_id='vel',
                                type=shared.ItemType.SECTION,
                            ),
                        ],
                        type=shared.ItemType.SECTION,
                        user_ids=[
                            6798.8,
                        ],
                    ),
                    shared.Step(
                        assigned_to=[
                            'esse',
                            'harum',
                            'iusto',
                            'ipsum',
                        ],
                        automation_config=shared.StepAutomationConfig(
                            flow_id='quisquam',
                        ),
                        due_date='2021-04-27T12:00:00.000Z',
                        dynamic_due_date=shared.DynamicDueDate(
                            action_type_condition=shared.DynamicDueDateActionTypeCondition.STEP_CLOSED,
                            number_of_units=2294.42,
                            step_id='tempore',
                            time_period=shared.DynamicDueDateTimePeriod.MONTHS,
                        ),
                        ecp=shared.ECPDetails(
                            label='numquam',
                        ),
                        execution_type=shared.StepType.MANUAL,
                        id='3f870b32-6b5a-4734-a9cd-b1a8422bb679',
                        name='Shawn Doyle',
                        order=4880.56,
                        requirements=[
                            shared.StepRequirement(
                                condition=shared.StepRequirementCondition.CLOSED,
                                definition_id='ullam',
                                type=shared.ItemType.SECTION,
                            ),
                        ],
                        type=shared.ItemType.SECTION,
                        user_ids=[
                            7653.26,
                        ],
                    ),
                    shared.Step(
                        assigned_to=[
                            'nobis',
                            'et',
                            'saepe',
                        ],
                        automation_config=shared.StepAutomationConfig(
                            flow_id='ipsum',
                        ),
                        due_date='2021-04-27T12:00:00.000Z',
                        dynamic_due_date=shared.DynamicDueDate(
                            action_type_condition=shared.DynamicDueDateActionTypeCondition.WORKFLOW_STARTED,
                            number_of_units=7492.55,
                            step_id='quos',
                            time_period=shared.DynamicDueDateTimePeriod.MONTHS,
                        ),
                        ecp=shared.ECPDetails(
                            label='cupiditate',
                        ),
                        execution_type=shared.StepType.MANUAL,
                        id='f3443a11-08e0-4adc-b4b9-21879fce953f',
                        name='Victoria Thiel',
                        order=9413.78,
                        requirements=[
                            shared.StepRequirement(
                                condition=shared.StepRequirementCondition.CLOSED,
                                definition_id='quod',
                                type=shared.ItemType.STEP,
                            ),
                            shared.StepRequirement(
                                condition=shared.StepRequirementCondition.CLOSED,
                                definition_id='similique',
                                type=shared.ItemType.SECTION,
                            ),
                            shared.StepRequirement(
                                condition=shared.StepRequirementCondition.CLOSED,
                                definition_id='vero',
                                type=shared.ItemType.STEP,
                            ),
                        ],
                        type=shared.ItemType.STEP,
                        user_ids=[
                            8489.44,
                            1943.42,
                            6178.77,
                            7733.26,
                        ],
                    ),
                ],
                type=shared.ItemType.STEP,
            ),
            shared.Step(
                assigned_to=[
                    'nulla',
                    'fugit',
                ],
                automation_config=shared.StepAutomationConfig(
                    flow_id='porro',
                ),
                due_date='2021-04-27T12:00:00.000Z',
                dynamic_due_date=shared.DynamicDueDate(
                    action_type_condition=shared.DynamicDueDateActionTypeCondition.STEP_CLOSED,
                    number_of_units=9850.33,
                    step_id='iusto',
                    time_period=shared.DynamicDueDateTimePeriod.MONTHS,
                ),
                ecp=shared.ECPDetails(
                    label='ducimus',
                ),
                execution_type=shared.StepType.MANUAL,
                id='a45626d4-3681-43f1-ad9f-5fce6c556146',
                name='Glenn Walter',
                order=534.27,
                requirements=[
                    shared.StepRequirement(
                        condition=shared.StepRequirementCondition.CLOSED,
                        definition_id='libero',
                        type=shared.ItemType.STEP,
                    ),
                    shared.StepRequirement(
                        condition=shared.StepRequirementCondition.CLOSED,
                        definition_id='aut',
                        type=shared.ItemType.SECTION,
                    ),
                    shared.StepRequirement(
                        condition=shared.StepRequirementCondition.CLOSED,
                        definition_id='impedit',
                        type=shared.ItemType.STEP,
                    ),
                    shared.StepRequirement(
                        condition=shared.StepRequirementCondition.CLOSED,
                        definition_id='fugit',
                        type=shared.ItemType.SECTION,
                    ),
                ],
                type=shared.ItemType.STEP,
                user_ids=[
                    896.03,
                    6774.12,
                ],
            ),
        ],
        id='ac366c8d-d6b1-4442-9074-74778a7bd466',
        last_update_time='2021-04-27T12:01:13.000Z',
        name='Alan Lang Jr.',
        update_entity_attributes=[
            shared.UpdateEntityAttributes(
                source=shared.UpdateEntityAttributesSource.CURRENT_STEP,
                target=shared.UpdateEntityAttributesTarget(
                    entity_attribute='my_status',
                    entity_schema='opportunity',
                ),
            ),
            shared.UpdateEntityAttributes(
                source=shared.UpdateEntityAttributesSource.WORKFLOW_STATUS,
                target=shared.UpdateEntityAttributesTarget(
                    entity_attribute='my_status',
                    entity_schema='opportunity',
                ),
            ),
            shared.UpdateEntityAttributes(
                source=shared.UpdateEntityAttributesSource.CURRENT_STEP,
                target=shared.UpdateEntityAttributesTarget(
                    entity_attribute='my_status',
                    entity_schema='opportunity',
                ),
            ),
        ],
        user_ids=[
            7774.08,
            6813.59,
            2594.22,
            1783.67,
        ],
    ),
    definition_id='voluptas',
)

res = s.workflows.update_definition(req)

if res.workflow_definition is not None:
    # handle response
```
