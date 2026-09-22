<?php
/**
 * Crown Movers — Phase 1 ACF field groups.
 *
 * Source of truth: Crown_Movers_Content_Architecture_Spec_v2.md §5.1 (Area
 * Details) and §5.3 (Service Details). Registered as local field groups so
 * they're version-controlled instead of hand-entered in ACF Pro's UI; ACF
 * still lets an admin override/sync from the UI if needed.
 *
 * Deliberately NOT included here (out of scope for this rebuild — no branch
 * or route template exists in bricks/ yet): §5.2 Branch Details, §5.4 Route
 * Details, §5.5 Global ACF Options. Build those when the branch page
 * template (spec §3.2 — required for /montreal-movers/ and
 * /fr/demenagement-montreal/, not part of the original 18-file pack) is
 * actually built.
 *
 * Requires ACF Pro (for the Repeater field type) and the CPT/taxonomy
 * registrations in 01-post-types-and-taxonomies.php.
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

add_action( 'acf/init', function () {
	if ( ! function_exists( 'acf_add_local_field_group' ) ) {
		return;
	}

	/**
	 * Area Details — location CPT (§5.1).
	 *
	 * Removed from the superseded pre-v2 spec and intentionally NOT
	 * reintroduced here: nap_override and a geo/map field. Publishing an
	 * address or coordinates on a page where Crown Movers has no premises
	 * is misleading structured data. NAP must come from the branch record
	 * via serving_branch below, never entered directly on a location post.
	 */
	acf_add_local_field_group( [
		'key'      => 'group_crown_area_details',
		'title'    => 'Area Details',
		'fields'   => [
			[
				'key'      => 'field_area_name',
				'label'    => 'Area name',
				'name'     => 'area_name',
				'type'     => 'text',
				'required' => 1,
				'instructions' => 'Drives H1, title, breadcrumb, and areaServed schema.',
			],
			[
				'key'      => 'field_area_type',
				'label'    => 'Area type',
				'name'     => 'area_type',
				'type'     => 'select',
				'required' => 1,
				'choices'  => [
					'city'    => 'City',
					'borough' => 'Borough',
					'region'  => 'Region',
				],
				'instructions' => 'Controls template variant and copy pattern.',
			],
			[
				'key'      => 'field_hero_heading',
				'label'    => 'Hero heading',
				'name'     => 'hero_heading',
				'type'     => 'text',
				'required' => 1,
			],
			[
				'key'      => 'field_hero_image',
				'label'    => 'Hero image',
				'name'     => 'hero_image',
				'type'     => 'image',
				'return_format' => 'id',
				'instructions'  => 'Falls back to a regional default — do not force a unique image on all ~267 pages.',
			],
			[
				'key'      => 'field_local_intro',
				'label'    => 'Local intro',
				'name'     => 'local_intro',
				'type'     => 'wysiwyg',
				'required' => 1,
				'instructions' => 'Must be genuinely local to this area — thin-content gate, spec §12.3. Do not reuse the same paragraph with the city name swapped.',
			],
			[
				'key'    => 'field_local_points',
				'label'  => 'Local detail points',
				'name'   => 'local_points',
				'type'   => 'repeater',
				'layout' => 'block',
				'instructions' => 'Access constraints, parking/permit notes, building types, seasonal notes.',
				'sub_fields' => [
					[ 'key' => 'field_local_points_title', 'label' => 'Title', 'name' => 'title', 'type' => 'text' ],
					[ 'key' => 'field_local_points_text', 'label' => 'Text', 'name' => 'text', 'type' => 'textarea' ],
				],
			],
			[
				'key'    => 'field_sub_areas',
				'label'  => 'Sectors / neighbourhoods',
				'name'   => 'sub_areas',
				'type'   => 'repeater',
				'layout' => 'table',
				'instructions' => 'Long-tail coverage mentioned in copy only — does not generate pages.',
				'sub_fields' => [
					[ 'key' => 'field_sub_areas_name', 'label' => 'Name', 'name' => 'name', 'type' => 'text' ],
				],
			],
			[
				'key'           => 'field_serving_branch',
				'label'         => 'Nearest branch',
				'name'          => 'serving_branch',
				'type'          => 'post_object',
				'post_type'     => [ 'page' ],
				'required'      => 1,
				'return_format' => 'id',
				'instructions'  => 'Select the branch Page (Montreal today; Toronto once verified — spec §3.2). Drives "served from" copy, drive-time context, and correct NAP display. Set once per location and audited at migration — this is the one deliberate Post Object relationship the spec keeps (§7.3).',
			],
			[
				'key'    => 'field_faqs',
				'label'  => 'Local FAQ',
				'name'   => 'faqs',
				'type'   => 'repeater',
				'layout' => 'block',
				'instructions' => 'Rendered as a visible accordion (bricks/06-faq.json pattern). FAQPage schema is optional and harmless, never the reason this field exists (spec §8.2 — Google removed FAQ rich results May 2026).',
				'sub_fields' => [
					[ 'key' => 'field_faqs_question', 'label' => 'Question', 'name' => 'question', 'type' => 'text' ],
					[ 'key' => 'field_faqs_answer', 'label' => 'Answer', 'name' => 'answer', 'type' => 'textarea' ],
				],
			],
			[
				'key'    => 'field_local_proof',
				'label'  => 'Local proof',
				'name'   => 'local_proof',
				'type'   => 'repeater',
				'layout' => 'block',
				'instructions' => 'Only real, attributable customer feedback (spec §8.3). Displayed as content only — never emit Review/AggregateRating schema for self-published testimonials.',
				'sub_fields' => [
					[ 'key' => 'field_local_proof_text', 'label' => 'Text', 'name' => 'text', 'type' => 'textarea' ],
					[ 'key' => 'field_local_proof_attribution', 'label' => 'Attribution', 'name' => 'attribution', 'type' => 'text' ],
				],
			],
			[
				'key'     => 'field_form_variant_location',
				'label'   => 'Quote form variant',
				'name'    => 'form_variant',
				'type'    => 'select',
				'choices' => [
					'standard'      => 'Standard',
					'long_distance' => 'Long-distance',
					'commercial'    => 'Commercial',
				],
				'instructions' => 'Passes this area into the quote form for lead attribution once WS Form / the n8n destination is wired (see bricks/05-quote-form.json — currently blocked, no endpoint exists yet).',
			],
			[
				'key'           => 'field_is_indexable',
				'label'         => 'Index this page',
				'name'          => 'is_indexable',
				'type'          => 'true_false',
				'default_value' => 1,
				'instructions'  => 'Feeds the thin-content gate (spec §12.3). When off, Rank Math should noindex this page and it should drop out of internal "nearby locations" loops.',
			],
		],
		'location' => [
			[
				[ 'param' => 'post_type', 'operator' => '==', 'value' => 'location' ],
			],
		],
	] );

	/**
	 * Service Details — Pages tagged with the "Service" page template
	 * (§5.3). Phase 1: services stay Pages, not a CPT (§3.5) — this field
	 * group is what makes a Page a "service" in the admin; the
	 * service_category taxonomy (registered in 01-post-types-and-taxonomies.php)
	 * is what the Bricks frontend template and the services-listing loop
	 * actually key off. Tag every service Page with both.
	 *
	 * Not included, per spec: related_services / areas_served as ACF
	 * Relationship fields — replaced by taxonomy query loops (§7.3) so nothing
	 * needs to be re-linked as pages are added.
	 */
	acf_add_local_field_group( [
		'key'    => 'group_crown_service_details',
		'title'  => 'Service Details',
		'fields' => [
			[ 'key' => 'field_service_hero_heading', 'label' => 'Hero heading', 'name' => 'hero_heading', 'type' => 'text' ],
			[ 'key' => 'field_service_hero_subheading', 'label' => 'Hero subheading', 'name' => 'hero_subheading', 'type' => 'text' ],
			[ 'key' => 'field_service_hero_image', 'label' => 'Hero image', 'name' => 'hero_image', 'type' => 'image', 'return_format' => 'id' ],
			[ 'key' => 'field_service_overview', 'label' => 'Overview', 'name' => 'overview', 'type' => 'wysiwyg' ],
			[
				'key'    => 'field_service_features',
				'label'  => 'Features',
				'name'   => 'features',
				'type'   => 'repeater',
				'layout' => 'block',
				'sub_fields' => [
					[ 'key' => 'field_service_features_icon', 'label' => 'Icon', 'name' => 'icon', 'type' => 'text', 'instructions' => 'Icon library key, matched to the icon element in bricks/12-single-service.json.' ],
					[ 'key' => 'field_service_features_title', 'label' => 'Title', 'name' => 'title', 'type' => 'text' ],
					[ 'key' => 'field_service_features_text', 'label' => 'Text', 'name' => 'text', 'type' => 'textarea' ],
				],
			],
			[
				'key'    => 'field_service_process_steps',
				'label'  => 'Process steps',
				'name'   => 'process_steps',
				'type'   => 'repeater',
				'layout' => 'block',
				'instructions' => 'Renders into the numbered "How it works" section already built in bricks/12-single-service.json.',
				'sub_fields' => [
					[ 'key' => 'field_service_process_steps_title', 'label' => 'Title', 'name' => 'title', 'type' => 'text' ],
					[ 'key' => 'field_service_process_steps_text', 'label' => 'Text', 'name' => 'text', 'type' => 'textarea' ],
				],
			],
			[
				'key'    => 'field_service_whats_included',
				'label'  => "What's included",
				'name'   => 'whats_included',
				'type'   => 'repeater',
				'layout' => 'table',
				'sub_fields' => [
					[ 'key' => 'field_service_whats_included_text', 'label' => 'Item', 'name' => 'text', 'type' => 'text' ],
				],
			],
			[
				'key'   => 'field_service_pricing_note',
				'label' => 'Pricing note',
				'name'  => 'pricing_note',
				'type'  => 'wysiwyg',
				'instructions' => 'May only contain figures Crown Movers supplies in writing. No estimated or derived pricing — [VERIFICATION REQUIRED] per spec §5.4/§9.',
			],
			[
				'key'    => 'field_service_faqs',
				'label'  => 'FAQ',
				'name'   => 'faqs',
				'type'   => 'repeater',
				'layout' => 'block',
				'sub_fields' => [
					[ 'key' => 'field_service_faqs_question', 'label' => 'Question', 'name' => 'question', 'type' => 'text' ],
					[ 'key' => 'field_service_faqs_answer', 'label' => 'Answer', 'name' => 'answer', 'type' => 'textarea' ],
				],
			],
			[
				'key'     => 'field_service_quote_form_variant',
				'label'   => 'Quote form variant',
				'name'    => 'quote_form_variant',
				'type'    => 'select',
				'choices' => [
					'standard'      => 'Standard',
					'long_distance' => 'Long-distance',
					'commercial'    => 'Commercial',
				],
			],
		],
		'location' => [
			[
				[ 'param' => 'page_template', 'operator' => '==', 'value' => 'crown-service-template.php' ],
			],
		],
	] );
} );
