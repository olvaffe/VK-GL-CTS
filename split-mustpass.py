#!/usr/bin/python3

SKIPLIST = [
    'dEQP-VK.api.info.device.properties',
    'dEQP-VK.info.device_extensions',
    'dEQP-VK.geometry.layered.3d.render_to_default_layer',
    'dEQP-VK.glsl.derivate.dfdxcoarse.texture.msaa4.vec2_highp',
    'dEQP-VK.glsl.derivate.fwidth.texture.msaa4.vec2_highp',
    'dEQP-VK.graphicsfuzz.function-with-uniform-return',
    'dEQP-VK.memory.pipeline_barrier.transfer_src_transfer_dst.1048576',
    'dEQP-VK.pipeline.render_to_image.core.1d_array.huge',
    'dEQP-VK.pipeline.render_to_image.core.2d_array.huge',
    'dEQP-VK.pipeline.render_to_image.core.3d.huge',
    'dEQP-VK.rasterization.interpolation_multisample_2_bit.lines_wide',
    'dEQP-VK.rasterization.interpolation_multisample_2_bit.non_strict_lines_wide',
    'dEQP-VK.rasterization.interpolation_multisample_4_bit.lines_wide',
    'dEQP-VK.rasterization.interpolation_multisample_4_bit.non_strict_lines_wide',
    'dEQP-VK.rasterization.interpolation_multisample_8_bit.lines_wide',
    'dEQP-VK.rasterization.interpolation_multisample_8_bit.non_strict_lines_wide',
    'dEQP-VK.spirv_assembly.instruction.compute.signed_int_compare.uint_slessthanequal',
    'dEQP-VK.wsi.display.get_display_plane_capabilities2',
    'dEQP-VK.wsi.xcb.display_timing',
    'dEQP-VK.wsi.xcb.incremental_present',
    'dEQP-VK.wsi.xcb.surface',
    'dEQP-VK.wsi.xcb.swapchain',
    'dEQP-VK.wsi.xlib.display_timing',
    'dEQP-VK.wsi.xlib.incremental_present',
    'dEQP-VK.wsi.xlib.surface',
    'dEQP-VK.wsi.xlib.swapchain',
]

with open('external/vulkancts/mustpass/master/vk-default.txt') as f:
    files = {}
    for line in f:
        test_case = line.strip()
        if test_case in SKIPLIST:
            continue
        if '.wayland.' in test_case:
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
