#!/usr/bin/python3

SKIPLIST = [
    'dEQP-VK.api.copy_and_blit.core.blit_image.simple_tests.mirror_z_3d.nearest',
    'dEQP-VK.api.copy_and_blit.core.blit_image.simple_tests.mirror_z_3d.r32_sfloat_nearest',
    'dEQP-VK.api.copy_and_blit.core.blit_image.simple_tests.mirror_z_3d.b8g8r8a8_unorm_nearest',
    'dEQP-VK.api.copy_and_blit.core.blit_image.simple_tests.mirror_z_3d.linear',
    'dEQP-VK.api.copy_and_blit.core.blit_image.simple_tests.mirror_z_3d.r32_sfloat_linear',
    'dEQP-VK.api.copy_and_blit.core.blit_image.simple_tests.mirror_z_3d.b8g8r8a8_unorm_linear',
    'dEQP-VK.api.copy_and_blit.core.blit_image.simple_tests.mirror_z_3d.cubic',
    'dEQP-VK.api.copy_and_blit.core.blit_image.simple_tests.mirror_z_3d.r32_sfloat_cubic',
    'dEQP-VK.api.copy_and_blit.core.blit_image.simple_tests.mirror_z_3d.b8g8r8a8_unorm_cubic',
    'dEQP-VK.api.copy_and_blit.dedicated_allocation.blit_image.simple_tests.mirror_z_3d.nearest',
    'dEQP-VK.api.copy_and_blit.dedicated_allocation.blit_image.simple_tests.mirror_z_3d.r32_sfloat_nearest',
    'dEQP-VK.api.copy_and_blit.dedicated_allocation.blit_image.simple_tests.mirror_z_3d.b8g8r8a8_unorm_nearest',
    'dEQP-VK.api.copy_and_blit.dedicated_allocation.blit_image.simple_tests.mirror_z_3d.linear',
    'dEQP-VK.api.copy_and_blit.dedicated_allocation.blit_image.simple_tests.mirror_z_3d.r32_sfloat_linear',
    'dEQP-VK.api.copy_and_blit.dedicated_allocation.blit_image.simple_tests.mirror_z_3d.b8g8r8a8_unorm_linear',
    'dEQP-VK.api.copy_and_blit.dedicated_allocation.blit_image.simple_tests.mirror_z_3d.cubic',
    'dEQP-VK.api.copy_and_blit.dedicated_allocation.blit_image.simple_tests.mirror_z_3d.r32_sfloat_cubic',
    'dEQP-VK.api.copy_and_blit.dedicated_allocation.blit_image.simple_tests.mirror_z_3d.b8g8r8a8_unorm_cubic',
    'dEQP-VK.subgroups.ballot_broadcast.graphics.subgroupbroadcast_i8vec3',
    'dEQP-VK.subgroups.ballot_broadcast.graphics.subgroupbroadcast_u8vec3',
    'dEQP-VK.subgroups.ballot_broadcast.graphics.subgroupbroadcast_i16vec3',
    'dEQP-VK.subgroups.ballot_broadcast.graphics.subgroupbroadcast_i16vec4',
    'dEQP-VK.subgroups.ballot_broadcast.graphics.subgroupbroadcast_u16vec3',
    'dEQP-VK.subgroups.ballot_broadcast.graphics.subgroupbroadcast_u16vec4',
    'dEQP-VK.subgroups.ballot_broadcast.compute.subgroupbroadcast_i8vec3',
    'dEQP-VK.subgroups.ballot_broadcast.compute.subgroupbroadcast_u8vec3',
    'dEQP-VK.subgroups.ballot_broadcast.compute.subgroupbroadcast_i16vec3',
    'dEQP-VK.subgroups.ballot_broadcast.compute.subgroupbroadcast_i16vec4',
    'dEQP-VK.subgroups.ballot_broadcast.compute.subgroupbroadcast_u16vec3',
    'dEQP-VK.subgroups.ballot_broadcast.compute.subgroupbroadcast_u16vec4',
    'dEQP-VK.subgroups.ballot_broadcast.framebuffer.subgroupbroadcast_i8vec3vertex',
    'dEQP-VK.subgroups.ballot_broadcast.framebuffer.subgroupbroadcast_i8vec3tess_eval',
    'dEQP-VK.subgroups.ballot_broadcast.framebuffer.subgroupbroadcast_i8vec3tess_control',
    'dEQP-VK.subgroups.ballot_broadcast.framebuffer.subgroupbroadcast_i8vec3geometry',
    'dEQP-VK.subgroups.ballot_broadcast.framebuffer.subgroupbroadcast_u8vec3vertex',
    'dEQP-VK.subgroups.ballot_broadcast.framebuffer.subgroupbroadcast_u8vec3tess_eval',
    'dEQP-VK.subgroups.ballot_broadcast.framebuffer.subgroupbroadcast_u8vec3tess_control',
    'dEQP-VK.subgroups.ballot_broadcast.framebuffer.subgroupbroadcast_u8vec3geometry',
    'dEQP-VK.subgroups.ballot_broadcast.framebuffer.subgroupbroadcast_i16vec3vertex',
    'dEQP-VK.subgroups.ballot_broadcast.framebuffer.subgroupbroadcast_i16vec3tess_eval',
    'dEQP-VK.subgroups.ballot_broadcast.framebuffer.subgroupbroadcast_i16vec3tess_control',
    'dEQP-VK.subgroups.ballot_broadcast.framebuffer.subgroupbroadcast_i16vec3geometry',
    'dEQP-VK.subgroups.ballot_broadcast.framebuffer.subgroupbroadcast_i16vec4vertex',
    'dEQP-VK.subgroups.ballot_broadcast.framebuffer.subgroupbroadcast_i16vec4tess_eval',
    'dEQP-VK.subgroups.ballot_broadcast.framebuffer.subgroupbroadcast_i16vec4tess_control',
    'dEQP-VK.subgroups.ballot_broadcast.framebuffer.subgroupbroadcast_i16vec4geometry',
    'dEQP-VK.subgroups.ballot_broadcast.framebuffer.subgroupbroadcast_u16vec3vertex',
    'dEQP-VK.subgroups.ballot_broadcast.framebuffer.subgroupbroadcast_u16vec3tess_eval',
    'dEQP-VK.subgroups.ballot_broadcast.framebuffer.subgroupbroadcast_u16vec3tess_control',
    'dEQP-VK.subgroups.ballot_broadcast.framebuffer.subgroupbroadcast_u16vec3geometry',
    'dEQP-VK.subgroups.ballot_broadcast.framebuffer.subgroupbroadcast_u16vec4vertex',
    'dEQP-VK.subgroups.ballot_broadcast.framebuffer.subgroupbroadcast_u16vec4tess_eval',
    'dEQP-VK.subgroups.ballot_broadcast.framebuffer.subgroupbroadcast_u16vec4tess_control',
    'dEQP-VK.subgroups.ballot_broadcast.framebuffer.subgroupbroadcast_u16vec4geometry',
    'dEQP-VK.graphicsfuzz.function-with-uniform-return',
    'dEQP-VK.graphicsfuzz.spv-access-chains',
    'dEQP-VK.graphicsfuzz.spv-copy-object',
    'dEQP-VK.graphicsfuzz.spv-dead-break-and-unroll',
]

with open('external/vulkancts/mustpass/master/vk-default.txt') as f:
    files = {}
    for line in f:
        test_case = line.strip()
        if test_case in SKIPLIST:
            continue

        groups = test_case.split('.')

        if ((groups[1] == 'api' and groups[2] in ['copy_and_blit', 'image_clearing', 'info']) or
            (groups[1] == 'binding_model' and groups[2] in ['buffer_device_address', 'shader_access']) or
            (groups[1] == 'draw' and groups[2] in ['instanced']) or
            (groups[1] == 'glsl' and groups[2] in ['builtin', 'matrix', 'operator', 'texture_functions', 'texture_gather']) or
            (groups[1] == 'image' and groups[2] in ['format_reinterpret']) or
            (groups[1] == 'memory_model' and groups[2] in ['write_after_read']) or
            (groups[1] == 'pipeline' and groups[2] in ['image', 'image_view', 'sampler', 'stencil']) or
            (groups[1] == 'renderpass' and groups[2] in ['suballocation']) or
            (groups[1] == 'renderpass2' and groups[2] in ['suballocation']) or
            (groups[1] == 'robustness' and groups[2] in ['robustness2']) or
            (groups[1] == 'spirv_assembly' and groups[2] in ['instruction']) or
            (groups[1] == 'ssbo' and groups[2] in ['phys']) or
            (groups[1] == 'subgroups' and groups[2] in ['arithmetic', 'ballot_broadcast', 'clustered']) or
            (groups[1] == 'synchronization' and groups[2] in ['op', 'cross_instance']) or
            (groups[1] == 'texture' and groups[2] in ['filtering', 'explicit_lod']) or
            (groups[1] == 'ubo' and groups[2] in ['random']) or
            (groups[1] == 'wsi' and groups[2] in ['xcb', 'xlib'])):
            category = '.'.join(groups[:3])
        else:
            category = '.'.join(groups[:2])

        if category not in files:
            files[category] = open('mustpass-%s.txt' % category, 'w')

        print(test_case, file=files[category])

    for val in files.values():
        val.close()
