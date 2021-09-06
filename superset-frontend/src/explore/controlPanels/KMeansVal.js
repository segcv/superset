import { t, SupersetClient } from '@superset-ui/core';
// import { sections } from '@superset-ui/chart-controls';

const xx = ()=>{
  let ret = {};
  $.ajax({
    url:"/api/v1/ai/list",
    dataType: 'json',
    async:false,
    success:(data)=>{
      ret = data;
    }
  });
  return ret['data'];
}

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
            label: 'checkpoint name',
            validators: [],
            choices: xx(), //[[3, 'hello'], [4, 'hello2']],
            description: t('请选择合适的checkpoint!'),
            // default: 10
          },
        }],
      ],
    },
  ]
};