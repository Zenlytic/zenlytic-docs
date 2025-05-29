// @ts-check
// Note: type annotations allow type checking and IDEs autocompletion

const lightCodeTheme = require('prism-react-renderer/themes/github');
const darkCodeTheme = require('prism-react-renderer/themes/dracula');

const config = {
  title: 'Zenlytic Docs',
  tagline: 'Intelligent Analytics',
  url: 'https://docs.zenlytic.com',
  baseUrl: '/',
  onBrokenLinks: 'warn',
  onBrokenMarkdownLinks: 'warn',
  favicon: 'img/favicon.ico',
  organizationName: 'Zenlytic', // Usually your GitHub org/user name.
  projectName: 'zenlytic-docs', // Usually your repo name.
  trailingSlash: false,
  
  plugins: [
    [
      'docusaurus-node-polyfills', 
      { excludeAliases: ['console'] }
    ]
  ],

  presets: [
    [
      '@docusaurus/preset-classic',
      ({
        docs: {
          sidebarPath: require.resolve('./sidebars.js'),
          editUrl: 'https://github.com/Zenlytic/zenlytic-docs/blob/master/',
          routeBasePath: 'docs',
        },
        theme: {
          customCss: require.resolve('./src/css/custom.css'),
        },
      }),
    ],
  ],

  // Remove duplicate Algolia preconnect configurations
  stylesheets: [
    {
      href: 'https://029VIRGT6M-dsn.algolia.net',
      rel: 'preconnect',
      crossorigin: 'anonymous'
    }
  ],

  themeConfig:
   // /** @type {import('@docusaurus/types').ThemeConfig} */
    ({
      algolia: {
        appId: '029VIRGT6M',
        apiKey: '1664be1f8d2107ebb3040175ea87987e',
        indexName: 'DOCS',
        searchPagePath: 'search',
        contextualSearch: true,
        searchParameters: {
          distinct: 1
        },
      },
      colorMode: {
        defaultMode: 'dark',
        disableSwitch: false, 
        respectPrefersColorScheme: false,
      },
      navbar: {
        title: 'Zenlytic',
        logo: {
          alt: 'Zenlytic Logo',
          src: 'img/zenlytic-logo.jpeg',
          href: 'https://www.zenlytic.com',
          target: '_blank',
        },
        items: [
          {
            to: '/',
            position: 'left',
            label: 'Docs',
          },
        ],
      },
      footer: {
        style: 'dark',
        links: [
          {
            title: 'Docs',
            items: [
              {
             label: 'Documentation',
                to: '/',
              },
            ],
          },
          {
            title: 'Community',
            items: [
              {
                label: 'Stack Overflow',
                href: 'https://stackoverflow.com/questions/tagged/zenlytic',
              },
              {
                label: 'Twitter',
                href: 'https://twitter.com/pablankley',
              },
            ],
          },
          {
            title: 'More',
            items: [
              {
                label: 'GitHub',
                href: 'https://github.com/Zenlytic/metrics_layer',
              },
              {
                label: 'Zenlytic.com',
                href: 'https://www.zenlytic.com',
              },
            ],
          },
        ],
        copyright: `Copyright © ${new Date().getFullYear()} Ex Quanta, Inc.`,
      },
      prism: {
        theme: lightCodeTheme,
        darkTheme: darkCodeTheme,
      },
      titleDelimiter: '',

      //added
      metadata: [
        { name: 'description', content: 'Documentation for Zenlytic\'s Intelligent Analytics platform.' },
        { property: 'og:title', content: 'Zenlytic Docs - Intelligent Analytics' },
        { property: 'og:description', content: 'Documentation for Zenlytic\'s Intelligent Analytics platform.' },
        { property: 'og:image', content: 'https://docs.zenlytic.com/img/social-card.png' }, // Update this to your actual image path
        { property: 'og:url', content: 'https://docs.zenlytic.com' },
        { property: 'og:type', content: 'website' },
        { name: 'twitter:card', content: 'summary_large_image' },
        { name: 'twitter:title', content: 'Zenlytic Docs - Intelligent Analytics' },
        { name: 'twitter:description', content: 'Documentation for Zenlytic\'s Intelligent Analytics platform.' },
        { name: 'twitter:image', content: 'https://docs.zenlytic.com/img/social-card.png' } // Same as above
      ]
      //end of added
    }),
};

module.exports = config;
