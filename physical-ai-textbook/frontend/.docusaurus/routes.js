import React from 'react';
import ComponentCreator from '@docusaurus/ComponentCreator';

export default [
  {
    path: '/__docusaurus/debug',
    component: ComponentCreator('/__docusaurus/debug', '932'),
    exact: true
  },
  {
    path: '/__docusaurus/debug/config',
    component: ComponentCreator('/__docusaurus/debug/config', '5f8'),
    exact: true
  },
  {
    path: '/__docusaurus/debug/content',
    component: ComponentCreator('/__docusaurus/debug/content', 'a26'),
    exact: true
  },
  {
    path: '/__docusaurus/debug/globalData',
    component: ComponentCreator('/__docusaurus/debug/globalData', 'e0a'),
    exact: true
  },
  {
    path: '/__docusaurus/debug/metadata',
    component: ComponentCreator('/__docusaurus/debug/metadata', '493'),
    exact: true
  },
  {
    path: '/__docusaurus/debug/registry',
    component: ComponentCreator('/__docusaurus/debug/registry', 'df8'),
    exact: true
  },
  {
    path: '/__docusaurus/debug/routes',
    component: ComponentCreator('/__docusaurus/debug/routes', '106'),
    exact: true
  },
  {
    path: '/docs',
    component: ComponentCreator('/docs', 'bf6'),
    routes: [
      {
        path: '/docs',
        component: ComponentCreator('/docs', '64a'),
        routes: [
          {
            path: '/docs',
            component: ComponentCreator('/docs', '808'),
            routes: [
              {
                path: '/docs/intro',
                component: ComponentCreator('/docs/intro', '6e9'),
                exact: true,
                sidebar: "docs"
              },
              {
                path: '/docs/module-1/ros2',
                component: ComponentCreator('/docs/module-1/ros2', '80a'),
                exact: true,
                sidebar: "docs"
              },
              {
                path: '/docs/module-2/digital-twin',
                component: ComponentCreator('/docs/module-2/digital-twin', 'c35'),
                exact: true,
                sidebar: "docs"
              },
              {
                path: '/docs/module-3/ai-robot-brain',
                component: ComponentCreator('/docs/module-3/ai-robot-brain', '4de'),
                exact: true,
                sidebar: "docs"
              },
              {
                path: '/docs/module-4/vla',
                component: ComponentCreator('/docs/module-4/vla', 'd5c'),
                exact: true,
                sidebar: "docs"
              }
            ]
          }
        ]
      }
    ]
  },
  {
    path: '*',
    component: ComponentCreator('*'),
  },
];
