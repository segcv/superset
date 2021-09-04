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
  ],
  controlOverrides: {
    groupby: {
      multiple: false,
    },
  },
};