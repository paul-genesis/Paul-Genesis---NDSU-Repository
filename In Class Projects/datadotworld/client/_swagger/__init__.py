# coding: utf-8

"""
    data.world API

    # data.world in a nutshell  data.world is a productive, secure platform for modern data teamwork.  We bring together your data practitioners, subject matter experts, and other stakeholders by removing costly barriers to data discovery, comprehension, integration, and sharing.   Everything your team needs to quickly understand and use data stays with it.   Social features and integrations encourage collaborators to ask and answer questions, share discoveries, and coordinate closely while still using their preferred tools.  Our focus on interoperability helps you enhance your own data with data from any source, including our vast and growing library of free public datasets.   Sophisticated permissions, auditing features, and more make it easy to manage who views your data and what they do with it.  # Conventions  ## Authentication  All data.world API calls require an API token.   OAuth2 is the preferred and most secure method for authenticating users of your data.world applications. Visit our [oauth documentation](https://apidocs.data.world/toolkit/oauth) for additional information. Alternatively, you can obtain a token for _personal use or testing_ by navigating to your profile settings, under the Advanced tab ([https://data.world/settings/advanced](https://data.world/settings/advanced)).  Authentication must be provided in API requests via the `Authorization` header. For example, for a user whose API token is `my_api_token`, the request header should be `Authorization: Bearer my_api_token` (note the `Bearer` prefix).  ## Content type   By default, `application/json` is the content type used in request and response bodies. Exceptions are noted in respective endpoint documentation.  ## HTTPS only   Our APIs can only be accessed via HTTPS.  # Interested in building data.world apps?  Check out our [developer portal](https://apidocs.data.world) for tips on how to get started, tutorials, and to interact with the API endpoints right within your browser.

    OpenAPI spec version: 0.21.0
    Contact: help@data.world
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

# import models into sdk package
from .models.agent_hydration_dto import AgentHydrationDto
from .models.analysis_image import AnalysisImage
from .models.asset_status import AssetStatus
from .models.catalog_analysis_hydration_dto import CatalogAnalysisHydrationDto
from .models.catalog_analysis_request import CatalogAnalysisRequest
from .models.catalog_business_term_hydration_dto import CatalogBusinessTermHydrationDto
from .models.catalog_column_hydration_dto import CatalogColumnHydrationDto
from .models.catalog_column_request import CatalogColumnRequest
from .models.catalog_concept_hydration_dto import CatalogConceptHydrationDto
from .models.catalog_glossary_request import CatalogGlossaryRequest
from .models.catalog_hydration_dto import CatalogHydrationDto
from .models.catalog_id import CatalogId
from .models.catalog_request import CatalogRequest
from .models.catalog_table_hydration_dto import CatalogTableHydrationDto
from .models.catalog_table_request import CatalogTableRequest
from .models.concept_entry import ConceptEntry
from .models.connection_dto import ConnectionDto
from .models.create_dataset_response import CreateDatasetResponse
from .models.create_insight_response import CreateInsightResponse
from .models.create_project_response import CreateProjectResponse
from .models.create_query_request import CreateQueryRequest
from .models.create_response import CreateResponse
from .models.custom_dataset_or_project_metadata_request import CustomDatasetOrProjectMetadataRequest
from .models.database_credentials import DatabaseCredentials
from .models.database_dbo import DatabaseDbo
from .models.database_source_reference import DatabaseSourceReference
from .models.dataset_create_request import DatasetCreateRequest
from .models.dataset_hydration_dto import DatasetHydrationDto
from .models.dataset_identifier import DatasetIdentifier
from .models.dataset_patch_request import DatasetPatchRequest
from .models.dataset_put_request import DatasetPutRequest
from .models.dataset_summary_response import DatasetSummaryResponse
from .models.doi import Doi
from .models.edit_activities_result_dto import EditActivitiesResultDto
from .models.entry_type import EntryType
from .models.error_message import ErrorMessage
from .models.file_batch_update_request import FileBatchUpdateRequest
from .models.file_create_or_update_request import FileCreateOrUpdateRequest
from .models.file_create_request import FileCreateRequest
from .models.file_source_create_or_update_request import FileSourceCreateOrUpdateRequest
from .models.file_source_create_request import FileSourceCreateRequest
from .models.file_source_summary_response import FileSourceSummaryResponse
from .models.file_summary_response import FileSummaryResponse
from .models.insight_body import InsightBody
from .models.insight_create_request import InsightCreateRequest
from .models.insight_hydration_dto import InsightHydrationDto
from .models.insight_patch_request import InsightPatchRequest
from .models.insight_put_request import InsightPutRequest
from .models.insight_summary_response import InsightSummaryResponse
from .models.instant import Instant
from .models.json_node import JsonNode
from .models.linked_dataset_create_or_update_request import LinkedDatasetCreateOrUpdateRequest
from .models.linked_dataset_summary_response import LinkedDatasetSummaryResponse
from .models.metadata_resource_dto import MetadataResourceDto
from .models.oauth_token_reference import OauthTokenReference
from .models.paginated_connection_results import PaginatedConnectionResults
from .models.paginated_dataset_results import PaginatedDatasetResults
from .models.paginated_insight_results import PaginatedInsightResults
from .models.paginated_metadata_resource_results import PaginatedMetadataResourceResults
from .models.paginated_project_results import PaginatedProjectResults
from .models.paginated_query_results import PaginatedQueryResults
from .models.paginated_search_results_dto import PaginatedSearchResultsDto
from .models.paginated_subscription_results import PaginatedSubscriptionResults
from .models.project_create_request import ProjectCreateRequest
from .models.project_patch_request import ProjectPatchRequest
from .models.project_put_request import ProjectPutRequest
from .models.project_summary_response import ProjectSummaryResponse
from .models.query_parameter import QueryParameter
from .models.query_put_request import QueryPutRequest
from .models.query_summary_response import QuerySummaryResponse
from .models.range import Range
from .models.rdf_term import RdfTerm
from .models.relationship_create_or_delete_request import RelationshipCreateOrDeleteRequest
from .models.relationship_get_request import RelationshipGetRequest
from .models.relationship_get_table_request import RelationshipGetTableRequest
from .models.resource_relationship_dto import ResourceRelationshipDto
from .models.saved_query_execution_request import SavedQueryExecutionRequest
from .models.search_facet_result import SearchFacetResult
from .models.search_hydrations import SearchHydrations
from .models.search_request import SearchRequest
from .models.simple_search_request import SimpleSearchRequest
from .models.single_table_metadata_spec import SingleTableMetadataSpec
from .models.source_id import SourceId
from .models.sql_query_request import SqlQueryRequest
from .models.ssh_tunnel import SshTunnel
from .models.stream_schema import StreamSchema
from .models.stream_schema_patch_request import StreamSchemaPatchRequest
from .models.streams_resource import StreamsResource
from .models.subscription import Subscription
from .models.subscription_api_links import SubscriptionApiLinks
from .models.subscription_create_request import SubscriptionCreateRequest
from .models.subscription_links import SubscriptionLinks
from .models.success_message import SuccessMessage
from .models.table_batch_update_request import TableBatchUpdateRequest
from .models.table_create_or_update_request import TableCreateOrUpdateRequest
from .models.table_id import TableId
from .models.table_source_create_or_update_request import TableSourceCreateOrUpdateRequest
from .models.tag import Tag
from .models.user_data_response import UserDataResponse
from .models.user_identifier import UserIdentifier
from .models.web_authorization import WebAuthorization
from .models.web_credentials import WebCredentials

# import apis into sdk package
from .apis.connections_api import ConnectionsApi
from .apis.do_is_api import DOIsApi
from .apis.datasets_api import DatasetsApi
from .apis.files_api import FilesApi
from .apis.insights_api import InsightsApi
from .apis.metadataanalysis_api import MetadataanalysisApi
from .apis.metadatacollections_api import MetadatacollectionsApi
from .apis.metadatadata_api import MetadatadataApi
from .apis.metadataglossary_api import MetadataglossaryApi
from .apis.metadataproperties_api import MetadatapropertiesApi
from .apis.metadatarelationships_api import MetadatarelationshipsApi
from .apis.projects_api import ProjectsApi
from .apis.queries_api import QueriesApi
from .apis.search_api import SearchApi
from .apis.streams_api import StreamsApi
from .apis.tables_api import TablesApi
from .apis.user_api import UserApi
from .apis.users_api import UsersApi
from .apis.webhooks_api import WebhooksApi

# import ApiClient
from .api_client import ApiClient

from .configuration import Configuration

configuration = Configuration()
