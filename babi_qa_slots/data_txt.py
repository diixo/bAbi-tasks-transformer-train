import os


paths = {
    "en": {
        "qa9": {
            "test": "tasks_1-20_v1-2/en/qa9_simple-negation_test.txt",
            "train": "tasks_1-20_v1-2/en/qa9_simple-negation_train.txt",
        },
        "qa4": {
            "train": "tasks_1-20_v1-2/en/qa4_two-arg-relations_train.txt",
            "test": "tasks_1-20_v1-2/en/qa4_two-arg-relations_test.txt",
        },
        "qa6": {
            "train": "tasks_1-20_v1-2/en/qa6_yes-no-questions_train.txt",
            "test": "tasks_1-20_v1-2/en/qa6_yes-no-questions_test.txt",
        },
        "qa11": {
            "test": "tasks_1-20_v1-2/en/qa11_basic-coreference_test.txt",
            "train": "tasks_1-20_v1-2/en/qa11_basic-coreference_train.txt",
        },
        "qa3": {
            "test": "tasks_1-20_v1-2/en/qa3_three-supporting-facts_test.txt",
            "train": "tasks_1-20_v1-2/en/qa3_three-supporting-facts_train.txt",
        },
        "qa15": {
            "test": "tasks_1-20_v1-2/en/qa15_basic-deduction_test.txt",
            "train": "tasks_1-20_v1-2/en/qa15_basic-deduction_train.txt",
        },
        "out.txt": {"out": "tasks_1-20_v1-2/en/out.txt"},
        "qa17": {
            "test": "tasks_1-20_v1-2/en/qa17_positional-reasoning_test.txt",
            "train": "tasks_1-20_v1-2/en/qa17_positional-reasoning_train.txt",
        },
        "qa13": {
            "test": "tasks_1-20_v1-2/en/qa13_compound-coreference_test.txt",
            "train": "tasks_1-20_v1-2/en/qa13_compound-coreference_train.txt",
        },
        "qa1": {
            "train": "tasks_1-20_v1-2/en/qa1_single-supporting-fact_train.txt",
            "test": "tasks_1-20_v1-2/en/qa1_single-supporting-fact_test.txt",
        },
        "qa14": {
            "train": "tasks_1-20_v1-2/en/qa14_time-reasoning_train.txt",
            "test": "tasks_1-20_v1-2/en/qa14_time-reasoning_test.txt",
        },
        "qa16": {
            "test": "tasks_1-20_v1-2/en/qa16_basic-induction_test.txt",
            "train": "tasks_1-20_v1-2/en/qa16_basic-induction_train.txt",
        },
        "qa19": {
            "test": "tasks_1-20_v1-2/en/qa19_path-finding_test.txt",
            "train": "tasks_1-20_v1-2/en/qa19_path-finding_train.txt",
        },
        "qa18": {
            "test": "tasks_1-20_v1-2/en/qa18_size-reasoning_test.txt",
            "train": "tasks_1-20_v1-2/en/qa18_size-reasoning_train.txt",
        },
        "qa10": {
            "train": "tasks_1-20_v1-2/en/qa10_indefinite-knowledge_train.txt",
            "test": "tasks_1-20_v1-2/en/qa10_indefinite-knowledge_test.txt",
        },
        "qa7": {
            "train": "tasks_1-20_v1-2/en/qa7_counting_train.txt",
            "test": "tasks_1-20_v1-2/en/qa7_counting_test.txt",
        },
        "qa5": {
            "test": "tasks_1-20_v1-2/en/qa5_three-arg-relations_test.txt",
            "train": "tasks_1-20_v1-2/en/qa5_three-arg-relations_train.txt",
        },
        "qa12": {
            "test": "tasks_1-20_v1-2/en/qa12_conjunction_test.txt",
            "train": "tasks_1-20_v1-2/en/qa12_conjunction_train.txt",
        },
        "qa2": {
            "train": "tasks_1-20_v1-2/en/qa2_two-supporting-facts_train.txt",
            "test": "tasks_1-20_v1-2/en/qa2_two-supporting-facts_test.txt",
        },
        "qa20": {
            "train": "tasks_1-20_v1-2/en/qa20_agents-motivations_train.txt",
            "test": "tasks_1-20_v1-2/en/qa20_agents-motivations_test.txt",
        },
        "qa8": {
            "train": "tasks_1-20_v1-2/en/qa8_lists-sets_train.txt",
            "test": "tasks_1-20_v1-2/en/qa8_lists-sets_test.txt",
        },
    },
    "en-10k": {
        "qa9": {
            "test": "tasks_1-20_v1-2/en-10k/qa9_simple-negation_test.txt",
            "train": "tasks_1-20_v1-2/en-10k/qa9_simple-negation_train.txt",
        },
        "qa4": {
            "train": "tasks_1-20_v1-2/en-10k/qa4_two-arg-relations_train.txt",
            "test": "tasks_1-20_v1-2/en-10k/qa4_two-arg-relations_test.txt",
        },
        "qa6": {
            "train": "tasks_1-20_v1-2/en-10k/qa6_yes-no-questions_train.txt",
            "test": "tasks_1-20_v1-2/en-10k/qa6_yes-no-questions_test.txt",
        },
        "qa11": {
            "test": "tasks_1-20_v1-2/en-10k/qa11_basic-coreference_test.txt",
            "train": "tasks_1-20_v1-2/en-10k/qa11_basic-coreference_train.txt",
        },
        "qa3": {
            "test": "tasks_1-20_v1-2/en-10k/qa3_three-supporting-facts_test.txt",
            "train": "tasks_1-20_v1-2/en-10k/qa3_three-supporting-facts_train.txt",
        },
        "qa15": {
            "test": "tasks_1-20_v1-2/en-10k/qa15_basic-deduction_test.txt",
            "train": "tasks_1-20_v1-2/en-10k/qa15_basic-deduction_train.txt",
        },
        "qa17": {
            "test": "tasks_1-20_v1-2/en-10k/qa17_positional-reasoning_test.txt",
            "train": "tasks_1-20_v1-2/en-10k/qa17_positional-reasoning_train.txt",
        },
        "qa13": {
            "test": "tasks_1-20_v1-2/en-10k/qa13_compound-coreference_test.txt",
            "train": "tasks_1-20_v1-2/en-10k/qa13_compound-coreference_train.txt",
        },
        "qa1": {
            "train": "tasks_1-20_v1-2/en-10k/qa1_single-supporting-fact_train.txt",
            "test": "tasks_1-20_v1-2/en-10k/qa1_single-supporting-fact_test.txt",
        },
        "qa14": {
            "train": "tasks_1-20_v1-2/en-10k/qa14_time-reasoning_train.txt",
            "test": "tasks_1-20_v1-2/en-10k/qa14_time-reasoning_test.txt",
        },
        "qa16": {
            "test": "tasks_1-20_v1-2/en-10k/qa16_basic-induction_test.txt",
            "train": "tasks_1-20_v1-2/en-10k/qa16_basic-induction_train.txt",
        },
        "qa19": {
            "test": "tasks_1-20_v1-2/en-10k/qa19_path-finding_test.txt",
            "train": "tasks_1-20_v1-2/en-10k/qa19_path-finding_train.txt",
        },
        "qa18": {
            "test": "tasks_1-20_v1-2/en-10k/qa18_size-reasoning_test.txt",
            "train": "tasks_1-20_v1-2/en-10k/qa18_size-reasoning_train.txt",
        },
        "qa10": {
            "train": "tasks_1-20_v1-2/en-10k/qa10_indefinite-knowledge_train.txt",
            "test": "tasks_1-20_v1-2/en-10k/qa10_indefinite-knowledge_test.txt",
        },
        "qa7": {
            "train": "tasks_1-20_v1-2/en-10k/qa7_counting_train.txt",
            "test": "tasks_1-20_v1-2/en-10k/qa7_counting_test.txt",
        },
        "qa5": {
            "test": "tasks_1-20_v1-2/en-10k/qa5_three-arg-relations_test.txt",
            "train": "tasks_1-20_v1-2/en-10k/qa5_three-arg-relations_train.txt",
        },
        "qa12": {
            "test": "tasks_1-20_v1-2/en-10k/qa12_conjunction_test.txt",
            "train": "tasks_1-20_v1-2/en-10k/qa12_conjunction_train.txt",
        },
        "qa2": {
            "train": "tasks_1-20_v1-2/en-10k/qa2_two-supporting-facts_train.txt",
            "test": "tasks_1-20_v1-2/en-10k/qa2_two-supporting-facts_test.txt",
        },
        "qa20": {
            "train": "tasks_1-20_v1-2/en-10k/qa20_agents-motivations_train.txt",
            "test": "tasks_1-20_v1-2/en-10k/qa20_agents-motivations_test.txt",
        },
        "qa8": {
            "train": "tasks_1-20_v1-2/en-10k/qa8_lists-sets_train.txt",
            "test": "tasks_1-20_v1-2/en-10k/qa8_lists-sets_test.txt",
        },
    },
    "en-valid": {
        "qa5": {
            "train": "tasks_1-20_v1-2/en-valid/qa5_train.txt",
            "test": "tasks_1-20_v1-2/en-valid/qa5_test.txt",
            "valid": "tasks_1-20_v1-2/en-valid/qa5_valid.txt",
        },
        "qa16": {
            "valid": "tasks_1-20_v1-2/en-valid/qa16_valid.txt",
            "test": "tasks_1-20_v1-2/en-valid/qa16_test.txt",
            "train": "tasks_1-20_v1-2/en-valid/qa16_train.txt",
        },
        "qa2": {
            "valid": "tasks_1-20_v1-2/en-valid/qa2_valid.txt",
            "test": "tasks_1-20_v1-2/en-valid/qa2_test.txt",
            "train": "tasks_1-20_v1-2/en-valid/qa2_train.txt",
        },
        "qa15": {
            "train": "tasks_1-20_v1-2/en-valid/qa15_train.txt",
            "test": "tasks_1-20_v1-2/en-valid/qa15_test.txt",
            "valid": "tasks_1-20_v1-2/en-valid/qa15_valid.txt",
        },
        "qa9": {
            "test": "tasks_1-20_v1-2/en-valid/qa9_test.txt",
            "train": "tasks_1-20_v1-2/en-valid/qa9_train.txt",
            "valid": "tasks_1-20_v1-2/en-valid/qa9_valid.txt",
        },
        "qa1": {
            "valid": "tasks_1-20_v1-2/en-valid/qa1_valid.txt",
            "test": "tasks_1-20_v1-2/en-valid/qa1_test.txt",
            "train": "tasks_1-20_v1-2/en-valid/qa1_train.txt",
        },
        "qa4": {
            "test": "tasks_1-20_v1-2/en-valid/qa4_test.txt",
            "train": "tasks_1-20_v1-2/en-valid/qa4_train.txt",
            "valid": "tasks_1-20_v1-2/en-valid/qa4_valid.txt",
        },
        "qa14": {
            "valid": "tasks_1-20_v1-2/en-valid/qa14_valid.txt",
            "train": "tasks_1-20_v1-2/en-valid/qa14_train.txt",
            "test": "tasks_1-20_v1-2/en-valid/qa14_test.txt",
        },
        "qa3": {
            "test": "tasks_1-20_v1-2/en-valid/qa3_test.txt",
            "train": "tasks_1-20_v1-2/en-valid/qa3_train.txt",
            "valid": "tasks_1-20_v1-2/en-valid/qa3_valid.txt",
        },
        "qa6": {
            "valid": "tasks_1-20_v1-2/en-valid/qa6_valid.txt",
            "test": "tasks_1-20_v1-2/en-valid/qa6_test.txt",
            "train": "tasks_1-20_v1-2/en-valid/qa6_train.txt",
        },
        "qa8": {
            "test": "tasks_1-20_v1-2/en-valid/qa8_test.txt",
            "valid": "tasks_1-20_v1-2/en-valid/qa8_valid.txt",
            "train": "tasks_1-20_v1-2/en-valid/qa8_train.txt",
        },
        "qa20": {
            "train": "tasks_1-20_v1-2/en-valid/qa20_train.txt",
            "valid": "tasks_1-20_v1-2/en-valid/qa20_valid.txt",
            "test": "tasks_1-20_v1-2/en-valid/qa20_test.txt",
        },
        "qa11": {
            "test": "tasks_1-20_v1-2/en-valid/qa11_test.txt",
            "train": "tasks_1-20_v1-2/en-valid/qa11_train.txt",
            "valid": "tasks_1-20_v1-2/en-valid/qa11_valid.txt",
        },
        "qa12": {
            "test": "tasks_1-20_v1-2/en-valid/qa12_test.txt",
            "valid": "tasks_1-20_v1-2/en-valid/qa12_valid.txt",
            "train": "tasks_1-20_v1-2/en-valid/qa12_train.txt",
        },
        "qa13": {
            "test": "tasks_1-20_v1-2/en-valid/qa13_test.txt",
            "valid": "tasks_1-20_v1-2/en-valid/qa13_valid.txt",
            "train": "tasks_1-20_v1-2/en-valid/qa13_train.txt",
        },
        "qa7": {
            "train": "tasks_1-20_v1-2/en-valid/qa7_train.txt",
            "test": "tasks_1-20_v1-2/en-valid/qa7_test.txt",
            "valid": "tasks_1-20_v1-2/en-valid/qa7_valid.txt",
        },
        "qa19": {
            "valid": "tasks_1-20_v1-2/en-valid/qa19_valid.txt",
            "test": "tasks_1-20_v1-2/en-valid/qa19_test.txt",
            "train": "tasks_1-20_v1-2/en-valid/qa19_train.txt",
        },
        "qa17": {
            "train": "tasks_1-20_v1-2/en-valid/qa17_train.txt",
            "test": "tasks_1-20_v1-2/en-valid/qa17_test.txt",
            "valid": "tasks_1-20_v1-2/en-valid/qa17_valid.txt",
        },
        "qa10": {
            "test": "tasks_1-20_v1-2/en-valid/qa10_test.txt",
            "valid": "tasks_1-20_v1-2/en-valid/qa10_valid.txt",
            "train": "tasks_1-20_v1-2/en-valid/qa10_train.txt",
        },
        "qa18": {
            "valid": "tasks_1-20_v1-2/en-valid/qa18_valid.txt",
            "train": "tasks_1-20_v1-2/en-valid/qa18_train.txt",
            "test": "tasks_1-20_v1-2/en-valid/qa18_test.txt",
        },
    },
    "en-valid-10k": {
        "qa5": {
            "train": "tasks_1-20_v1-2/en-valid-10k/qa5_train.txt",
            "test": "tasks_1-20_v1-2/en-valid-10k/qa5_test.txt",
            "valid": "tasks_1-20_v1-2/en-valid-10k/qa5_valid.txt",
        },
        "qa16": {
            "valid": "tasks_1-20_v1-2/en-valid-10k/qa16_valid.txt",
            "test": "tasks_1-20_v1-2/en-valid-10k/qa16_test.txt",
            "train": "tasks_1-20_v1-2/en-valid-10k/qa16_train.txt",
        },
        "qa2": {
            "valid": "tasks_1-20_v1-2/en-valid-10k/qa2_valid.txt",
            "test": "tasks_1-20_v1-2/en-valid-10k/qa2_test.txt",
            "train": "tasks_1-20_v1-2/en-valid-10k/qa2_train.txt",
        },
        "qa15": {
            "train": "tasks_1-20_v1-2/en-valid-10k/qa15_train.txt",
            "test": "tasks_1-20_v1-2/en-valid-10k/qa15_test.txt",
            "valid": "tasks_1-20_v1-2/en-valid-10k/qa15_valid.txt",
        },
        "qa9": {
            "test": "tasks_1-20_v1-2/en-valid-10k/qa9_test.txt",
            "train": "tasks_1-20_v1-2/en-valid-10k/qa9_train.txt",
            "valid": "tasks_1-20_v1-2/en-valid-10k/qa9_valid.txt",
        },
        "qa1": {
            "valid": "tasks_1-20_v1-2/en-valid-10k/qa1_valid.txt",
            "test": "tasks_1-20_v1-2/en-valid-10k/qa1_test.txt",
            "train": "tasks_1-20_v1-2/en-valid-10k/qa1_train.txt",
        },
        "qa4": {
            "test": "tasks_1-20_v1-2/en-valid-10k/qa4_test.txt",
            "train": "tasks_1-20_v1-2/en-valid-10k/qa4_train.txt",
            "valid": "tasks_1-20_v1-2/en-valid-10k/qa4_valid.txt",
        },
        "qa14": {
            "valid": "tasks_1-20_v1-2/en-valid-10k/qa14_valid.txt",
            "train": "tasks_1-20_v1-2/en-valid-10k/qa14_train.txt",
            "test": "tasks_1-20_v1-2/en-valid-10k/qa14_test.txt",
        },
        "qa3": {
            "test": "tasks_1-20_v1-2/en-valid-10k/qa3_test.txt",
            "train": "tasks_1-20_v1-2/en-valid-10k/qa3_train.txt",
            "valid": "tasks_1-20_v1-2/en-valid-10k/qa3_valid.txt",
        },
        "qa6": {
            "valid": "tasks_1-20_v1-2/en-valid-10k/qa6_valid.txt",
            "test": "tasks_1-20_v1-2/en-valid-10k/qa6_test.txt",
            "train": "tasks_1-20_v1-2/en-valid-10k/qa6_train.txt",
        },
        "qa8": {
            "test": "tasks_1-20_v1-2/en-valid-10k/qa8_test.txt",
            "valid": "tasks_1-20_v1-2/en-valid-10k/qa8_valid.txt",
            "train": "tasks_1-20_v1-2/en-valid-10k/qa8_train.txt",
        },
        "qa20": {
            "train": "tasks_1-20_v1-2/en-valid-10k/qa20_train.txt",
            "valid": "tasks_1-20_v1-2/en-valid-10k/qa20_valid.txt",
            "test": "tasks_1-20_v1-2/en-valid-10k/qa20_test.txt",
        },
        "qa11": {
            "test": "tasks_1-20_v1-2/en-valid-10k/qa11_test.txt",
            "train": "tasks_1-20_v1-2/en-valid-10k/qa11_train.txt",
            "valid": "tasks_1-20_v1-2/en-valid-10k/qa11_valid.txt",
        },
        "qa12": {
            "test": "tasks_1-20_v1-2/en-valid-10k/qa12_test.txt",
            "valid": "tasks_1-20_v1-2/en-valid-10k/qa12_valid.txt",
            "train": "tasks_1-20_v1-2/en-valid-10k/qa12_train.txt",
        },
        "qa13": {
            "test": "tasks_1-20_v1-2/en-valid-10k/qa13_test.txt",
            "valid": "tasks_1-20_v1-2/en-valid-10k/qa13_valid.txt",
            "train": "tasks_1-20_v1-2/en-valid-10k/qa13_train.txt",
        },
        "qa7": {
            "train": "tasks_1-20_v1-2/en-valid-10k/qa7_train.txt",
            "test": "tasks_1-20_v1-2/en-valid-10k/qa7_test.txt",
            "valid": "tasks_1-20_v1-2/en-valid-10k/qa7_valid.txt",
        },
        "qa19": {
            "valid": "tasks_1-20_v1-2/en-valid-10k/qa19_valid.txt",
            "test": "tasks_1-20_v1-2/en-valid-10k/qa19_test.txt",
            "train": "tasks_1-20_v1-2/en-valid-10k/qa19_train.txt",
        },
        "qa17": {
            "train": "tasks_1-20_v1-2/en-valid-10k/qa17_train.txt",
            "test": "tasks_1-20_v1-2/en-valid-10k/qa17_test.txt",
            "valid": "tasks_1-20_v1-2/en-valid-10k/qa17_valid.txt",
        },
        "qa10": {
            "test": "tasks_1-20_v1-2/en-valid-10k/qa10_test.txt",
            "valid": "tasks_1-20_v1-2/en-valid-10k/qa10_valid.txt",
            "train": "tasks_1-20_v1-2/en-valid-10k/qa10_train.txt",
        },
        "qa18": {
            "valid": "tasks_1-20_v1-2/en-valid-10k/qa18_valid.txt",
            "train": "tasks_1-20_v1-2/en-valid-10k/qa18_train.txt",
            "test": "tasks_1-20_v1-2/en-valid-10k/qa18_test.txt",
        },
    },
    "shuffled": {
        "qa9": {
            "test": "tasks_1-20_v1-2/shuffled/qa9_simple-negation_test.txt",
            "train": "tasks_1-20_v1-2/shuffled/qa9_simple-negation_train.txt",
        },
        "qa4": {
            "train": "tasks_1-20_v1-2/shuffled/qa4_two-arg-relations_train.txt",
            "test": "tasks_1-20_v1-2/shuffled/qa4_two-arg-relations_test.txt",
        },
        "qa6": {
            "train": "tasks_1-20_v1-2/shuffled/qa6_yes-no-questions_train.txt",
            "test": "tasks_1-20_v1-2/shuffled/qa6_yes-no-questions_test.txt",
        },
        "qa11": {
            "test": "tasks_1-20_v1-2/shuffled/qa11_basic-coreference_test.txt",
            "train": "tasks_1-20_v1-2/shuffled/qa11_basic-coreference_train.txt",
        },
        "qa3": {
            "test": "tasks_1-20_v1-2/shuffled/qa3_three-supporting-facts_test.txt",
            "train": "tasks_1-20_v1-2/shuffled/qa3_three-supporting-facts_train.txt",
        },
        "qa15": {
            "test": "tasks_1-20_v1-2/shuffled/qa15_basic-deduction_test.txt",
            "train": "tasks_1-20_v1-2/shuffled/qa15_basic-deduction_train.txt",
        },
        "qa17": {
            "test": "tasks_1-20_v1-2/shuffled/qa17_positional-reasoning_test.txt",
            "train": "tasks_1-20_v1-2/shuffled/qa17_positional-reasoning_train.txt",
        },
        "qa13": {
            "test": "tasks_1-20_v1-2/shuffled/qa13_compound-coreference_test.txt",
            "train": "tasks_1-20_v1-2/shuffled/qa13_compound-coreference_train.txt",
        },
        "qa1": {
            "train": "tasks_1-20_v1-2/shuffled/qa1_single-supporting-fact_train.txt",
            "test": "tasks_1-20_v1-2/shuffled/qa1_single-supporting-fact_test.txt",
        },
        "qa14": {
            "train": "tasks_1-20_v1-2/shuffled/qa14_time-reasoning_train.txt",
            "test": "tasks_1-20_v1-2/shuffled/qa14_time-reasoning_test.txt",
        },
        "qa16": {
            "test": "tasks_1-20_v1-2/shuffled/qa16_basic-induction_test.txt",
            "train": "tasks_1-20_v1-2/shuffled/qa16_basic-induction_train.txt",
        },
        "qa19": {
            "test": "tasks_1-20_v1-2/shuffled/qa19_path-finding_test.txt",
            "train": "tasks_1-20_v1-2/shuffled/qa19_path-finding_train.txt",
        },
        "qa18": {
            "test": "tasks_1-20_v1-2/shuffled/qa18_size-reasoning_test.txt",
            "train": "tasks_1-20_v1-2/shuffled/qa18_size-reasoning_train.txt",
        },
        "qa10": {
            "train": "tasks_1-20_v1-2/shuffled/qa10_indefinite-knowledge_train.txt",
            "test": "tasks_1-20_v1-2/shuffled/qa10_indefinite-knowledge_test.txt",
        },
        "qa7": {
            "train": "tasks_1-20_v1-2/shuffled/qa7_counting_train.txt",
            "test": "tasks_1-20_v1-2/shuffled/qa7_counting_test.txt",
        },
        "qa5": {
            "test": "tasks_1-20_v1-2/shuffled/qa5_three-arg-relations_test.txt",
            "train": "tasks_1-20_v1-2/shuffled/qa5_three-arg-relations_train.txt",
        },
        "qa12": {
            "test": "tasks_1-20_v1-2/shuffled/qa12_conjunction_test.txt",
            "train": "tasks_1-20_v1-2/shuffled/qa12_conjunction_train.txt",
        },
        "qa2": {
            "train": "tasks_1-20_v1-2/shuffled/qa2_two-supporting-facts_train.txt",
            "test": "tasks_1-20_v1-2/shuffled/qa2_two-supporting-facts_test.txt",
        },
        "qa20": {
            "train": "tasks_1-20_v1-2/shuffled/qa20_agents-motivations_train.txt",
            "test": "tasks_1-20_v1-2/shuffled/qa20_agents-motivations_test.txt",
        },
        "qa8": {
            "train": "tasks_1-20_v1-2/shuffled/qa8_lists-sets_train.txt",
            "test": "tasks_1-20_v1-2/shuffled/qa8_lists-sets_test.txt",
        },
    },
    "shuffled-10k": {
        "qa9": {
            "test": "tasks_1-20_v1-2/shuffled-10k/qa9_simple-negation_test.txt",
            "train": "tasks_1-20_v1-2/shuffled-10k/qa9_simple-negation_train.txt",
        },
        "qa4": {
            "train": "tasks_1-20_v1-2/shuffled-10k/qa4_two-arg-relations_train.txt",
            "test": "tasks_1-20_v1-2/shuffled-10k/qa4_two-arg-relations_test.txt",
        },
        "qa6": {
            "train": "tasks_1-20_v1-2/shuffled-10k/qa6_yes-no-questions_train.txt",
            "test": "tasks_1-20_v1-2/shuffled-10k/qa6_yes-no-questions_test.txt",
        },
        "qa11": {
            "test": "tasks_1-20_v1-2/shuffled-10k/qa11_basic-coreference_test.txt",
            "train": "tasks_1-20_v1-2/shuffled-10k/qa11_basic-coreference_train.txt",
        },
        "qa3": {
            "test": "tasks_1-20_v1-2/shuffled-10k/qa3_three-supporting-facts_test.txt",
            "train": "tasks_1-20_v1-2/shuffled-10k/qa3_three-supporting-facts_train.txt",
        },
        "qa15": {
            "test": "tasks_1-20_v1-2/shuffled-10k/qa15_basic-deduction_test.txt",
            "train": "tasks_1-20_v1-2/shuffled-10k/qa15_basic-deduction_train.txt",
        },
        "qa17": {
            "test": "tasks_1-20_v1-2/shuffled-10k/qa17_positional-reasoning_test.txt",
            "train": "tasks_1-20_v1-2/shuffled-10k/qa17_positional-reasoning_train.txt",
        },
        "qa13": {
            "test": "tasks_1-20_v1-2/shuffled-10k/qa13_compound-coreference_test.txt",
            "train": "tasks_1-20_v1-2/shuffled-10k/qa13_compound-coreference_train.txt",
        },
        "qa1": {
            "train": "tasks_1-20_v1-2/shuffled-10k/qa1_single-supporting-fact_train.txt",
            "test": "tasks_1-20_v1-2/shuffled-10k/qa1_single-supporting-fact_test.txt",
        },
        "qa14": {
            "train": "tasks_1-20_v1-2/shuffled-10k/qa14_time-reasoning_train.txt",
            "test": "tasks_1-20_v1-2/shuffled-10k/qa14_time-reasoning_test.txt",
        },
        "qa16": {
            "test": "tasks_1-20_v1-2/shuffled-10k/qa16_basic-induction_test.txt",
            "train": "tasks_1-20_v1-2/shuffled-10k/qa16_basic-induction_train.txt",
        },
        "qa19": {
            "test": "tasks_1-20_v1-2/shuffled-10k/qa19_path-finding_test.txt",
            "train": "tasks_1-20_v1-2/shuffled-10k/qa19_path-finding_train.txt",
        },
        "qa18": {
            "test": "tasks_1-20_v1-2/shuffled-10k/qa18_size-reasoning_test.txt",
            "train": "tasks_1-20_v1-2/shuffled-10k/qa18_size-reasoning_train.txt",
        },
        "qa10": {
            "train": "tasks_1-20_v1-2/shuffled-10k/qa10_indefinite-knowledge_train.txt",
            "test": "tasks_1-20_v1-2/shuffled-10k/qa10_indefinite-knowledge_test.txt",
        },
        "qa7": {
            "train": "tasks_1-20_v1-2/shuffled-10k/qa7_counting_train.txt",
            "test": "tasks_1-20_v1-2/shuffled-10k/qa7_counting_test.txt",
        },
        "qa5": {
            "test": "tasks_1-20_v1-2/shuffled-10k/qa5_three-arg-relations_test.txt",
            "train": "tasks_1-20_v1-2/shuffled-10k/qa5_three-arg-relations_train.txt",
        },
        "qa12": {
            "test": "tasks_1-20_v1-2/shuffled-10k/qa12_conjunction_test.txt",
            "train": "tasks_1-20_v1-2/shuffled-10k/qa12_conjunction_train.txt",
        },
        "qa2": {
            "train": "tasks_1-20_v1-2/shuffled-10k/qa2_two-supporting-facts_train.txt",
            "test": "tasks_1-20_v1-2/shuffled-10k/qa2_two-supporting-facts_test.txt",
        },
        "qa20": {
            "train": "tasks_1-20_v1-2/shuffled-10k/qa20_agents-motivations_train.txt",
            "test": "tasks_1-20_v1-2/shuffled-10k/qa20_agents-motivations_test.txt",
        },
        "qa8": {
            "train": "tasks_1-20_v1-2/shuffled-10k/qa8_lists-sets_train.txt",
            "test": "tasks_1-20_v1-2/shuffled-10k/qa8_lists-sets_test.txt",
        },
    },
}

def load_babi_txt(file_path: str) -> list:
    # "datasets/bAbI/en-10k/qa1_single-supporting-fact_train.txt"
    """
    Split bAbI txt specified file and return list of episodes:
    [{'story': ..., 'question': ..., 'answer': ...}, ...]
    """
    examples = []
    story_lines = []
    with open(file_path, 'r') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            # remove sentence number
            idx, text = line.split(' ', 1)
            idx = int(idx)

            if '\t' in text:  # check marker of question line
                question, answer, _ = text.split('\t')
                # construct prompt: whole history before question
                #story = ' '.join(story_lines)
                examples.append({
                    'story': story_lines,
                    'question': question,
                    'answer': answer
                })
            else:
                story_lines.append(text)

            # reset history by new episode (new marker == 1)
            if idx == 1:
                story_lines = [text]
    return examples


class BabiqaText():

    def __init__(self, tokenizer, task_no="qa1", split="train", ext=False) -> None:

        type_sz = "en-10k" if ext else "en"
        self.filepath = os.path.join(
            os.path.dirname(os.path.relpath(__file__)),
            paths[type_sz][task_no][split]
        )
        print(self.filepath)
        self.raw_text = load_babi_txt(self.filepath)
        self.tokenizer = tokenizer

    def get_raw_sz(self):
        return len(self.raw_text)


if __name__ == "__main__":

    babi = BabiqaText(None, "qa1", "train")
    print(babi.get_raw_sz())
    print(babi.filepath)
