{
  'includes': [
    'brightray.gypi',
  ],
  'targets': [
    {
      'target_name': 'brightray',
      'type': 'static_library',
      'include_dirs': [
        '.',
        '<(libchromiumcontent_include_dir)',
        '<(libchromiumcontent_include_dir)/third_party/skia/include/config',
      ],
      'direct_dependent_settings': {
        'include_dirs': [
          '..',
          '<(libchromiumcontent_include_dir)',
          '<(libchromiumcontent_include_dir)/third_party/skia/include/config',
        ],
      },
      'sources': [
        'browser/browser_client.cc',
        'browser/browser_client.h',
        'browser/browser_context.cc',
        'browser/browser_context.h',
        'browser/browser_main_parts.cc',
        'browser/browser_main_parts.h',
        'browser/browser_main_parts_mac.mm',
        'browser/default_web_contents_delegate.cc',
        'browser/default_web_contents_delegate.h',
        'browser/default_web_contents_delegate_mac.mm',
        'browser/devtools_delegate.cc',
        'browser/devtools_delegate.h',
        'browser/inspectable_web_contents.cc',
        'browser/inspectable_web_contents.h',
        'browser/inspectable_web_contents_impl.cc',
        'browser/inspectable_web_contents_impl.h',
        'browser/inspectable_web_contents_view.h',
        'browser/inspectable_web_contents_view_mac.h',
        'browser/inspectable_web_contents_view_mac.mm',
        'browser/mac/bry_application.h',
        'browser/mac/bry_application.mm',
        'browser/mac/bry_inspectable_web_contents_view.h',
        'browser/mac/bry_inspectable_web_contents_view.mm',
        'browser/mac/bry_inspectable_web_contents_view_private.h',
        'browser/network_delegate.cc',
        'browser/network_delegate.h',
        'browser/notification_presenter.h',
        'browser/notification_presenter_mac.h',
        'browser/notification_presenter_mac.mm',
        'browser/url_request_context_getter.cc',
        'browser/url_request_context_getter.h',
        'common/application_info.h',
        'common/application_info_mac.mm',
        'common/content_client.cc',
        'common/content_client.h',
        'common/mac/foundation_util.h',
        'common/mac/main_application_bundle.h',
        'common/mac/main_application_bundle.mm',
        'common/main_delegate.cc',
        'common/main_delegate.h',
        'common/main_delegate_mac.mm',
      ],
      'conditions': [
        ['OS=="mac"', {
          'link_settings': {
            'libraries': [
              'libchromiumcontent.dylib',
              '$(SDKROOT)/System/Library/Frameworks/AppKit.framework',
            ],
          },
        }],
        ['OS=="win"', {
          'link_settings': {
            'libraries': [
              '<(libchromiumcontent_library_dir)/chromiumcontent.dll.lib',
            ],
          },
        }],
      ],
    },
  ],
}
