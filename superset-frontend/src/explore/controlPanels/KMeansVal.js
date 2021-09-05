import { t } from '@superset-ui/core';
// import { sections } from '@superset-ui/chart-controls';

export default {
  controlPanelSections: [
    {
      label: t('Query'),
      expanded: true,
      controlSetRows: [
        ['columns'],
        ['adhoc_filters'],
      ],
    },
    {
      label: t('Model Options'),
      expanded: true,
      controlSetRows: [
        [{
          name: 'checkpoint_info',
          config: {
            type: 'SelectControl',
            freeForm: true,
            label: 'checkpoints',
            validators: [],
            choices: [],
            description: t('请选择合适的checkpoint!'),
            default: 10
          },
        }],
      ],
    },
  ]
};