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
        ['limit']
      ],
    },
    {
      label: t('Save Model'),
      expanded: true,
      controlSetRows: [
        [{
          name: 'max_num_clusters',
          config: {
            type: 'SelectControl',
            freeForm: true,
            label: 'max_num_clusters',
            validators: [],
            choices: [10, 20],
            description: t('设定肘方法的最大簇数！'),
            default: 10
          },
        }],
        [{
          name: 'num_clusters',
          config: {
            type: 'SelectControl',
            freeForm: true,
            label: 'num_clusters',
            validators: [],
            choices: [3],
            description: t('设定存储模型的簇数！'),
            default: 3
          },
        }],
        [
          {
            name: 'checkpoint_name',
            config: {
              type: 'TextControl',
              label: t('name of model checkpoint'),
              description: t(
                '设置模型存储入库的名称，以方便预测时使用！',
              ),
              default: 'kmeans',
            },
          },
        ],
      ],
    },
  ],
  controlOverrides: {
    groupby: {
      multiple: false,
    },
  },
};